# colab-server

This is the server part of the CoLab chat app.

#### Set up

To install the dependencies run `pip3 install requirements.txt`
Note that you need to create a database with `python3 manage.py create_db` to be able
to store user data.


##### Run

The server is currently hardcoded to serve to `127.0.0.1:5000`. We need
to make this dependent on the configuration type, ie `production`, `development` or `testing`.

The API of the api is/will be defined via `manage.py`. To run the server
`python3 manage.py runserver`. Inspect the page in a browser.


###### Lint

To perform lint checking, run `python3 manage.py lint`.