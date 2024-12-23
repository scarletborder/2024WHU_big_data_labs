from kafka import KafkaProducer
import random
import time
import datagen as datagen

# Kafka configuration
KAFKA_TOPIC = "example-topic"
KAFKA_BOOTSTRAP_SERVER = "kafka:9092"  # 替换为实际的 Kafka 服务器地址

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
    api_version=(0, 10, 2),
    value_serializer=lambda v: v.encode("utf-8"),
)

if __name__ == "__main__":
    print("Starting Kafka producer...")
    try:
        while True:
            # Generate CSV data and send to Kafka
            csv_data = datagen.generate_read_data("./example/ETTh1.csv")
            kafka_json = datagen.dump_dict_to_json(csv_data)
            producer.send(KAFKA_TOPIC, kafka_json)
            print(f"Sent data to Kafka:\n{kafka_json}") 

            # Sleep for a random interval between 1 and 5 seconds
            time.sleep(random.randint(1, 5))
    except KeyboardInterrupt:
        print("Kafka producer stopped.")
    finally:
        producer.close()
