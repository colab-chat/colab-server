#!/bin/sh

# TODO check if it makes sense to increase processes in a container.
uwsgi --http 0.0.0.0:8000 --module wsgi:application --processes 1 --threads 4
