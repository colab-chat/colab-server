from flask_script import Manager, Server
from colab_server import create_app, db

# --------------------------------
# Flask script manager
# This is the entry point of CoLab
# -------------------------------
manager = Manager(create_app)


# Set the server configuration TODO: parametrize this to adapt according to app.config
manager.add_command("runserver", Server(host="127.0.0.1", port=5000))


# --------------------------------
# Script commands
# --------------------------------
@manager.command
def create_db(drop_first=False):
    if drop_first:
        db.drop_all()
    db.create_all()


if __name__ == '__main__':
    manager.run()
