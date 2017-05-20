from colab_server import db
from flask_user import UserMixin


# ------------------------------
# User
# TODO: encrypt password
# -----------------------------
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # Account info
    email = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
    confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')

    # General details
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')

    # Personal details
    first_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    last_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    team = db.Column(db.Unicode(50), nullable=False, server_default=u'')
