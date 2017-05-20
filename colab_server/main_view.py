from flask import Blueprint, render_template, request


# -------------------------------
# Main blueprint
# -------------------------------
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
def index():
    if request.method == 'POST':
        print("POST")
    else:
        print("GET")
    return render_template('index.html',
                           app_name="CoLab",
                           message='this is a message')
