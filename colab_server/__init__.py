from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail

from config import config

# ----------------
# Flask extensions
# ----------------
db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()

# Taken from Miguel's Flack app, Why do we need this?
from . import models  # noqa


def create_app(config_name=None):
    # ------------------------
    # Set up colab_server configuration
    # ------------------------
    if config_name is None:
        config_name = 'development'
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # ---------------------------
    # Initialize flask extensions
    # ---------------------------
    db.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)

    # -----
    # Login
    # -----

    # ---------------------------
    # Registration of blue prints
    # ---------------------------
    from .main_view import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth_view import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/user")

    return app
