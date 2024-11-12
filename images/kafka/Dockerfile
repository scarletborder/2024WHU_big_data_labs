FROM java:openjdk-8-jre
LABEL author="xuqinghan"
LABEL purpose = 'kafka'

# ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y wget

RUN wget -q http://mirrors.hust.edu.cn/apache/kafka/1.0.0/kafka_2.11-1.0.0.tgz
RUN tar -xzf kafka_2.11-1.0.0.tgz -C /home
RUN mv /home/kafka_2.11-1.0.0 /kafka
WORKDIR /kafka
#CMD ["/bin/bash"]
CMD ["/kafka/bin/kafka-server-start.sh", "/kafka/config/server.properties"]
