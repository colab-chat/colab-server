FROM python:3.5.3

ARG LIBRDKAFKA_VER="0.9.5"

RUN apt-get -y update

# librdkafka build deps:
RUN apt-get -y install build-essential zlib1g-dev unzip
ADD https://github.com/edenhill/librdkafka/archive/v$LIBRDKAFKA_VER.zip /tmp/source.zip
RUN cd /tmp && \
    unzip source.zip && mv librdkafka-* librdkafka && \
    cd /tmp/librdkafka && \
    ./configure && \
    make all && make install && \
    make clean && ./configure --clean

RUN apt-get -y install python3-cffi python3-dev

WORKDIR /build

ENV BUILD_PACKAGES "build-essential git curl zlib1g-dev python"
RUN apt-get update -y
RUN apt-get install $BUILD_PACKAGES -y
RUN git clone https://github.com/edenhill/kafkacat.git
RUN cd kafkacat && \
    ./bootstrap.sh && \
    make install && \
    cd .. && rm -rf kafkacat
RUN AUTO_ADDED_PACKAGES=`apt-mark showauto`
RUN apt-get remove --purge -y $BUILD_PACKAGES $AUTO_ADDED_PACKAGES
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#  Transfer code
RUN mkdir /colab
ADD . /colab
WORKDIR /colab

RUN pip install -r requirements.txt

CMD ["./boot.sh"]
