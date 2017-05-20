""" Registers the user handling functionality with the app"""
from .view import auth as auth_blueprint
from flask_user import (UserManager, SQLAlchemyAdapter)
from .forms import CoLabRegisterForm
from .models import User


def setup_auth(app, db):
    # Register the blueprint with the app
    app.register_blueprint(auth_blueprint, url_prefix="/user")

    # Register the user manager with the app
    db_adapter = SQLAlchemyAdapter(db, User)
    _ = UserManager(db_adapter=db_adapter,
                    app=app,
                    register_form=CoLabRegisterForm)
