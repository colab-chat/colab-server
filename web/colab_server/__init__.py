from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_sse import sse
from flask_debugtoolbar import DebugToolbarExtension


# ----------------
# Flask extensions
# ----------------
db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()
debug_toolbar = DebugToolbarExtension()


def create_app(configuration):
    # ------------------------
    # Set up colab_server configuration
    # ------------------------
    if configuration is None:
        raise ValueError("Missing configuration for CoLab")
    app = Flask(__name__)
    app.config.from_object(configuration)
    print("Set up application with configuration for {}.".format(configuration.name))

    # ---------------------------
    # Initialize flask extensions
    # ---------------------------
    db.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    debug_toolbar.init_app(app)

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
