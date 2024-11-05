# Start with a basic Python image with Java and Hadoop support
FROM python:3.9-bookworm

# Install dependencies
RUN apt-get update
RUN /bin/sh -c set -eux; apt-get update; apt-get install -y --no-install-recommends wget ; rm -rf /var/lib/apt/lists/*

COPY ./hadoop-3.3.6.tar.gz ./hadoop-3.3.6.tar.gz

COPY ./java-8-openjdk-amd64/ /usr/lib/jvm/java-8-openjdk-amd64/

COPY ./glibc-2.38.tar.gz ./glibc-2.38.tar.gz

# Install Hadoop (necessary for Pydoop)
RUN tar -xzvf glibc-2.38.tar.gz && \
    mv glibc-2.38 /usr/local/glibc238 && \
    rm glibc-2.38.tar.gz

RUN tar -xzvf hadoop-3.3.6.tar.gz && \
    mv hadoop-3.3.6 /usr/local/hadoop && \
    rm hadoop-3.3.6.tar.gz

# Set environment variables for Hadoop
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
# ENV PATH=$PATH:$HADOOP_HOME/bin

RUN export PATH="/usr/local/hadoop/bin:/usr/local/hadoop/sbin:${PATH}"


RUN ln -s /usr/include/tirpc/rpc/* /usr/include/rpc/
RUN ln -s /usr/include/tirpc/netconfig.h /usr/include

# Install Python dependencies
COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

RUN pip install kafka-python

RUN cd /usr/local/glibc238
RUN mkdir build
RUN cd build
# RUN ../configure --prefix=/usr --disable-profile --enable-add-ons --with-headers=/usr/include --with-binutils=/usr/bin

RUN export PATH="/usr/local/hadoop/bin:/usr/local/hadoop/sbin:${PATH}"
# RUN pip install pydoop

# Set up the entrypoint
CMD ["/bin/sh"]