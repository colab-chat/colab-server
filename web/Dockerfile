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

#  Transfer code
RUN mkdir /colab
ADD . /colab
WORKDIR /colab

RUN pip install -r requirements.txt

CMD ["./boot.sh"]
