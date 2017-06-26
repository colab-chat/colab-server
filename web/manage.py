import subprocess
import sys
from functools import partial

from flask_script import Manager
from colab_server import create_app, db
from config import create_configuration

# --------------------------------
# Flask script manager
# -------------------------------
configuration = create_configuration()
app_with_configuration = partial(create_app, configuration)
manager = Manager(app_with_configuration)


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
    proc = subprocess.Popen(
        ['flake8', '--ignore=E402', 'colab_server/', 'manage.py', 'config.py',
         'wsgi.py'],
        stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    output, errors = proc.communicate()
    linting = proc.returncode == 0

    if linting:
        print('No linting issues.')
        sys.exit(0)
    else:
        print('flake8 found the following problems:')
        print(output.decode('utf-8'))
        sys.exit(1)


if __name__ == '__main__':
    manager.run()
