from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config


# ----------------
# Flask extensions
# ----------------
db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()


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

    # --------------------
    # Authentication setup
    # --------------------
    from .auth.setup_auth import setup_auth
    setup_auth(app, db)

    # -------------------------------
    # Registration of main blue print
    # -------------------------------
    from .main_view import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
