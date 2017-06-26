#!/bin/sh

# Wait for Kafka to be ready before starting the web app
kafkacat -b kafka -L
OUT=$?
i="0"
while [ $OUT -ne 0 -a  $i != 10  ]; do
   echo "Waiting for Kafka to be ready"
   sleep 1
   kafkacat -b kafka -L
   OUT=$?
   i=$[$i+1]
done

gunicorn wsgi:application --worker-class gevent --bind 0.0.0.0:8000
