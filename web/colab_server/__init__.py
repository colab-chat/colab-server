from flask import Flask
import logging
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from .flask_sse_kafka import sse

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

    # ---------------------------
    # Logger
    # ---------------------------
    file_handler = logging.FileHandler('web_log.txt')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    app.my_logger = logging.getLogger("app_logger")
    app.my_logger.addHandler(file_handler)
    app.my_logger.setLevel(logging.DEBUG)

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

    app.register_blueprint(sse, url_prefix="/stream")

    return app
