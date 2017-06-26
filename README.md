# colab-server

[![Build Status](https://travis-ci.org/colab-chat/colab-server.svg?branch=master)](https://travis-ci.org/colab-chat/colab-server)
[![License (GPL-3.0)](https://img.shields.io/badge/license-GPL%203.0-blue.svg)](https://github.com/colab-chat/colab-server/blob/master/LICENSE)

This is the server part of the CoLab chat app.

#### Set up

To install the python dependencies run `pip install -r requirements.txt`
Note that you need to create a database with `python ./web/manage.py create_db` to be able
to store user data.

You will also need to install docker and docker-compose. For example on Ubuntu:
```
sudo apt install docker
sudo apt install docker-compose
sudo usermod -aG docker $USER
```


##### Run

To start the webserver use `colab.py`.
To run in production mode you can either use `./colab.py` or `./colab.py -r prod` or `./colab.py --run prod`.
To run in development mode you can either use `./colab.py -r dev` or `./colab.py --run dev`.
To run in detached mode add `-d` or `--detached`.
To stop use `./colab.py -s` or `./colab.py --stop`.

If you don't stop the containers gracefully you may see the error "A broker is already registered on the path /brokers/ids/1." when restarting. This can be fixed by `docker-compose kill` then bring back up as normal.

The page is served to `localhost:80`.

Unit tests can be run with `./colab.py -r tests` after installing pytest with
```
pip install pytest
```

###### Lint

To perform lint checking, run `cd web && python manage.py lint`.
