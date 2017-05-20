from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class LoginForm(FlaskForm):
    """
    The login form has an id input (email) and a password input
    """
    email = StringField('Email', validators=[
        validators.DataRequired('Email is required'), validators.Email()])
    password = StringField('Password', validators=[
        validators.DataRequired('Password is required')])
    submit = SubmitField('Submit')
