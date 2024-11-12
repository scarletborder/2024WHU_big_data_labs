# 使用 Python 基础镜像
FROM crs4/pydoop-base:3.2.0-3.7

WORKDIR /app

# 安装 kafka-python 依赖
RUN pip install kafka-python

# 复制生产者代码
COPY . .

CMD ["python3", "main.py"]
