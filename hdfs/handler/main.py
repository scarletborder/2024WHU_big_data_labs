from kafka import KafkaConsumer
import json
import os
from utils.hdfs import *
from server.start import start_fastapi_server
from server.handler import Send_Data
import threading

print("handler start...\n")

# 连接 Kafka 的配置
bootstrap_servers = "kafka:9092"
group_id = (
    "power-consumers"  # 消费者组 ID，确保所有消费者使用相同的组 ID 以实现负载均衡
)

# 创建 KafkaConsumer 实例
consumer = KafkaConsumer(
    "city",
    bootstrap_servers=bootstrap_servers,
    # group_id=group_id,
    auto_offset_reset="earliest",  # 从最早的消息开始消费，适合初次启动时
    enable_auto_commit=True,  # 自动提交偏移量，确保消息不重复消费
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),  # 反序列化 JSON 数据
)

# 使用正则表达式订阅所有符合 "city-*" 命名的 topic
# consumer.subscribe(pattern="^city-.*")


def process_message(message):
    """
    处理消息的函数。在这里实现你处理每条消息的逻辑。
    """
    city = message.value.get("city")
    data = message.value.get("data")  # json data which came from a dict
    print(f"Processing data from city: {city}, data: {data}")
    # traverse from data handler
    res = Send_Data(data)
    print(res)


if __name__ == "__main__":
    # launch a fastapi server which allows to register data handler
    fastapi_thread = threading.Thread(target=start_fastapi_server)
    fastapi_thread.start()

    # 消费消息
    try:
        for message in consumer:
            print(
                f"Received message from Topic: {message.topic}, Partition: {message.partition}, Offset: {message.offset}"
            )
            process_message(message)
    except Exception as e:
        print(f"Error processing message: {e}")
    finally:
        consumer.close()
