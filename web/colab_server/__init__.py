from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy


# ----------------
# Flask extensions
# ----------------
db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()


def create_app(configuration):
    # ------------------------
    # Set up colab_server configuration
    # ------------------------
    if configuration is None:
        raise ValueError("Missing configuration for CoLab")
    app = Flask(__name__)
    app.config.from_object(configuration)

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
