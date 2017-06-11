#!/bin/sh

# Wait 15 seconds to make sure Kafka is ready before starting
sleep 15
gunicorn wsgi:application --worker-class gevent --bind 0.0.0.0:8000
