import subprocess
import sys

from flask_script import Manager, Server

from colab_server import create_app, db

# --------------------------------
# Flask script manager
# -------------------------------
manager = Manager(create_app)


# Set the server configuration TODO: parametrize this to adapt according
#                                    to app.config
# manager.add_command("runserver", Server(host="127.0.0.1", port=5000))


# --------------------------------
# Script commands
# --------------------------------
@manager.command
def create_db(drop_first=False):
    if drop_first:
        db.drop_all()
    db.create_all()


@manager.command
def drop_db():
    db.drop_all()


@manager.command
def lint():
    linting = subprocess.call(['flake8', '--ignore=E402', 'colab_server/',
                               'manage.py', 'config.py']) == 0
    if linting:
        print('No linting issues.')
    sys.exit(linting)


if __name__ == '__main__':
    manager.run()
