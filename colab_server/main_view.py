from flask import Blueprint, render_template


# -------------------------------
# Main blueprint
# -------------------------------
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html',
                           app_name="CoLab",
                           message='this is a message')
