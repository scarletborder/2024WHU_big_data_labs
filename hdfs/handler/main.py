from kafka import KafkaConsumer
import json


# Kafka configuration
KAFKA_TOPIC = "example-topic"
KAFKA_BOOTSTRAP_SERVER = "kafka:9092"  # 替换为实际的 Kafka 服务器地址


if __name__ == "__main__":

    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
    )
    data = []
    for msg in consumer:
        info = msg.value.decode("utf-8")
        data = json.loads(info)
        print(data)
