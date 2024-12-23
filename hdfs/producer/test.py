from kafka import KafkaProducer
import time
import json
import os
from datagen import generate_read_data

# from utils import generate_csv_data  # 确保 utils 包含此函数

# 连接 Kafka，并设置生产者的幂等性、重试和批处理配置
producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    retries=5,  # 设置重试次数
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),  # 序列化为 JSON
)

# 从环境变量或默认值中获取 Kafka Topic
city_name = os.getenv("CITY_NAME", "Hefei")  # 使用城市名称而非固定 topic
kafka_topic = f"example-topic"


def emit():
    for send_data in generate_read_data("example/ETTh1.csv"):
        print(f"send message {send_data}")

        # 将数据打包为 JSON 格式，并指定城市名称作为分区键
        producer.send(
            kafka_topic,
            # key=city_name.encode("utf-8"),  # 使用城市名称作为分区键
            value={
                "data": send_data,
                "city": city_name,
            },  # 包含数据和城市信息的 JSON 对象
        )
        time.sleep(15)  # 模拟间隔发送


if __name__ == "__main__":
    emit()

    # 发送完消息后刷新并关闭生产者
    producer.flush()
    producer.close()
