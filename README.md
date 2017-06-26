# colab-server

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
To run in production mode you can either use `./colab.py` or `./colab.py -r 0` or `./colab.py --run 0`.
To run in development mode you can either use `./colab.py -r 1` or `./colab.py --run 1`.
To run in detached mode add `-d` or `--detached`.
To stop use `./colab.py -s` or `./colab.py --stop`.

If you don't stop the containers gracefully you may see the error "A broker is already registered on the path /brokers/ids/1." when restarting. This can be fixed by `docker-compose kill` then bring back up as normal.

Testing environment support is to come.
 
The page is served to `localhost:80`.

###### Lint

To perform lint checking, run `cd web && python manage.py lint`.
