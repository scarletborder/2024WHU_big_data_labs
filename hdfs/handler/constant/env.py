import os
import pydoop

HDFS_URI = os.getenv("HDFS_URI", "hdfs://namenode:9000")
HDFS_PATH = os.getenv("HDFS_PATH", "/example/hadoop/uploads")
