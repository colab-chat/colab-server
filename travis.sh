#!/usr/bin/env bash

VER="0.9.5"

echo "....fetching librdkafka dependency...."
mkdir tmp_build
cd tmp_build
wget https://github.com/edenhill/librdkafka/archive/v${VER}.tar.gz
tar -zxf v${VER}.tar.gz
echo ".....done....."
cd librdkafka-${VER}
echo "....compiling librdkafka...."
./configure && make
sudo make install
echo "....done...."
cd ../../
echo ".... ensure librdkafka is available....."
sudo ldconfig
rm -Rf tmp_build
