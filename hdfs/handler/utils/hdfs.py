from io import StringIO
import json
import pydoop.hdfs as hdfs
from datetime import datetime


def HDFSUpload(city: str, csv_string: str):
    # Split the CSV data into lines
    lines = csv_string.strip().split("\n")

    # Extract the headers
    headers = lines[0].split(",")
    headers = [_.strip() for _ in headers]

    for line in lines[1:]:
        values = line.split(",")
        values = [_.strip() for _ in values]

        # 假设date是0th 元素
        time_str = values[0]
        time_obj = datetime.strptime(time_str, "%Y-%m-%d.%H:%M:%S")
        entry = {headers[i]: values[i] for i in range(len(headers))}
        AppendJson(city, entry, time_obj)
        ...


def AppendJson(city: str, entry: dict, time_obj: datetime):
    hdfs_directory = (
        f"/data/power_station/{city}/{time_obj.year}/{time_obj.month}/{time_obj.day}"
    )
    hdfs_file_path = f"{hdfs_directory}/{time_obj.hour}.csv"

    # # 如果 HDFS 目录不存在，创建目录
    # if not hdfs.path.exists(hdfs_directory):
    #     hdfs.mkdir(hdfs_directory)

    print(
        f"""
hdfs_directory{hdfs_directory}              
hdfs_file_path:{hdfs_file_path}
data:{entry}
"""
    )

    # # 将数据追加到基于城市和时间的 HDFS 文件中
    # with hdfs.open(hdfs_file_path, 'at') as f:
    # f.write(new_data + '\n')  # 每条数据以换行符结尾，确保数据格式正确
