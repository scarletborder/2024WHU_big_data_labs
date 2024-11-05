from kafka import KafkaProducer
import random
import time
import csv
import io
from datetime import datetime, timedelta

# Kafka configuration
KAFKA_TOPIC = "example-topic"
KAFKA_BOOTSTRAP_SERVER = "kafka:9092"  # 替换为实际的 Kafka 服务器地址

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
    value_serializer=lambda v: v.encode("utf-8"),
)


def generate_random_data():
    """Generate a random date, temperature, and pressure."""
    # Generate random date within the past 30 days
    date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")

    # Generate random temperature and pressure values
    temperature = round(
        random.uniform(-10, 35), 2
    )  # Temperature between -10 and 35 degrees Celsius
    pressure = round(random.uniform(950, 1050), 2)  # Pressure between 950 and 1050 hPa

    return {"date": date, "temperature": temperature, "pressure": pressure}


def generate_csv_data():
    """Generate CSV formatted data."""
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["date", "temperature", "pressure"])

    # Write header
    writer.writeheader()

    # Generate and write random data rows
    for _ in range(random.randint(1, 5)):  # Generate between 1 and 5 rows of data
        writer.writerow(generate_random_data())

    return output.getvalue()


if __name__ == "__main__":
    print("Starting Kafka producer...")
    try:
        while True:
            # Generate CSV data and send to Kafka
            csv_data = generate_csv_data()
            producer.send(KAFKA_TOPIC, csv_data)
            print(f"Sent data to Kafka:\n{csv_data}")

            # Sleep for a random interval between 1 and 5 seconds
            time.sleep(random.randint(1, 5))
    except KeyboardInterrupt:
        print("Kafka producer stopped.")
    finally:
        producer.close()
