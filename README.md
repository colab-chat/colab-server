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

To start the webserver: `docker-compose up -d`.
The page is served to `loacalhost:80` running with `production` settings. More generic settings
are to come. In addition to `production` we will support `development` and `testing`.


###### Lint

To perform lint checking, run `python ./web/manage.py lint`.
