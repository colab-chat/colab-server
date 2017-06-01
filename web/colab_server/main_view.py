from flask import Blueprint, render_template
from flask_user import login_required
from flask_sse import sse

# -------------------------------
# Main blueprint
# -------------------------------
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
@login_required
def index():
    print("INDEX PAGE")
    return render_template('index.html')


@main.route('/hello')
def publish_hello():
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"
