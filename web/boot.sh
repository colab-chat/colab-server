#!/bin/sh

# TODO check if it makes sense to increase processes in a container.
# uwsgi --http 0.0.0.0:8000 --module wsgi:application  --gevent 100
gunicorn wsgi:application --worker-class gevent --bind 0.0.0.0:8000
