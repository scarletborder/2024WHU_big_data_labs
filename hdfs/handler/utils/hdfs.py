# Utils about interact with hdfs

from kafka import KafkaConsumer
import pydoop.hdfs as hdfs
import csv
import os
import io

# Kafka and HDFS configuration
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "example-topic")
KAFKA_BOOTSTRAP_SERVER = os.getenv("KAFKA_BOOTSTRAP_SERVER", "kafka:9092")
HDFS_PATH = os.getenv("HDFS_PATH", "/example/hadoop/uploads")

# Initialize Kafka consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
)


def process_csv_data(csv_data):
    """Process CSV data from each message and prepare for HDFS storage"""
    csvfile = io.StringIO(csv_data)
    reader = csv.reader(csvfile)
    headers = next(reader)  # Assume first row is the header

    processed_data = []
    for row in reader:
        processed_data.append(dict(zip(headers, row)))

    return processed_data


def write_to_hdfs(data, file_name):
    """Write data to HDFS in CSV format using Pydoop"""
    file_path = f"{HDFS_PATH}/{file_name}"
    with hdfs.open(file_path, "w") as writer:
        writer.write(data)


if __name__ == "__main__":
    print("Starting HDFS Handler with Pydoop...")

    for message in consumer:
        csv_data = message.value.decode("utf-8")
        print("Received CSV data")

        processed_data = process_csv_data(csv_data)
        file_name = (
            f"data_{message.offset}.csv"  # Unique file name based on Kafka offset
        )

        # Convert processed data back to CSV format for HDFS storage
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=processed_data[0].keys())
        writer.writeheader()
        writer.writerows(processed_data)

        write_to_hdfs(output.getvalue(), file_name)
        print(f"Data written to HDFS at {HDFS_PATH}/{file_name}")
