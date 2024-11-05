import pydoop.hdfs as hdfs
import time
import os

# HDFS configuration
HDFS_URI = os.getenv("HDFS_URI", "hdfs://namenode:9000")
HDFS_PATH = os.getenv("HDFS_PATH", "/example/hadoop/uploads")


def read_and_print_hdfs_data():
    """Read data from HDFS and print to console."""
    # List files in the HDFS directory
    try:
        files = hdfs.ls(HDFS_PATH)
    except Exception as e:
        print(f"Failed to list files in HDFS path {HDFS_PATH}: {e}")
        return

    # Read and print each file's contents
    for file_path in files:
        try:
            with hdfs.open(file_path, "r") as f:
                data = f.read().decode("utf-8")
                print(f"Data from {file_path}:\n{data}")
        except Exception as e:
            print(f"Failed to read file {file_path}: {e}")


if __name__ == "__main__":
    print("Starting User Service (read from HDFS and print)...")

    # Periodically read and print data from HDFS
    while True:
        read_and_print_hdfs_data()
        time.sleep(10)  # Sleep for 10 seconds before reading again
