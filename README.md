# colab-server

This is the server part of the CoLab chat app.

#### Set up

To install the dependencies run `pip3 install requirements.txt`
Note that you need to create a database with `python3 ./web/manage.py create_db` to be able
to store user data.


##### Run

To start the webserver: `docker-compose up -d`.
The page is served to `loacalhost:80` running with `production` settings. More generic settings
are to come. In addition to `production` we will support `development` and `testing`.


###### Lint

To perform lint checking, run `python3 ./web/manage.py lint`.