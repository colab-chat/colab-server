# colab-server

This is the server part of the CoLab chat app.

#### Set up

To install the dependencies run `pip3 install -r requirements.txt`
Note that you need to create a database with `python3 ./web/manage.py create_db` to be able
to store user data.


##### Run

To start the webserver: `docker-compose up -d`.
The page is served to `loacalhost:80` running with `production` settings. More generic settings
are to come. In addition to `production` we will support `development` and `testing`.

If you don't stop the containers gracefully you may see the error "A broker is already registered on the path /brokers/ids/1." when restarting. This can be fixed by `docker-compose kill` then bring back up as normal.

###### Lint

To perform lint checking, run `python3 ./web/manage.py lint`.
