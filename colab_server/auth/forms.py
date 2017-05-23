from wtforms import StringField, validators
from flask_user.forms import (RegisterForm)


# ----------------------------------------
# Add customised authentication forms here
# ----------------------------------------
class CoLabRegisterForm(RegisterForm):
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])
