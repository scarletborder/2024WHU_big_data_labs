# 使用 Python 基础镜像
FROM python:3.9-bookworm

WORKDIR /app

RUN pip install grpcio grpcio-tools grpcio-reflection googleapis-common-protos
RUN pip install requests
RUN pip install "fastapi[standard]"

ENV PYTHONIOENCODING=utf-8

COPY . .

# RUN ../../proto ./proto/

# RUN ./summon_proto.sh

CMD ["sh","run.sh"]
