# 使用 Python 基础镜像
FROM python:3.9-slim

WORKDIR /app

# 安装 kafka-python 依赖
RUN pip install kafka-python

# 复制生产者代码
COPY . .

CMD ["python", "main.py"]
