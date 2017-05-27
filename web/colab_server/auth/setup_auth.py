""" Registers the user handling functionality with the app"""
from flask_user import (UserManager, SQLAlchemyAdapter)
from .forms import CoLabRegisterForm
from .models import User


def setup_auth(app, db):
    # Register the user manager with the app.
    # Each form that is customised needs to be added here.
    db_adapter = SQLAlchemyAdapter(db, User)
    _ = UserManager(db_adapter=db_adapter,  # noqa
                    app=app,
                    register_form=CoLabRegisterForm)
