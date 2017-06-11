#!/bin/sh

sleep 15
gunicorn wsgi:application --worker-class gevent --bind 0.0.0.0:8000
