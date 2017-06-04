from flask import Blueprint, render_template
from flask_user import login_required
from .flask_sse_kafka import sse

# -------------------------------
# Main blueprint
# -------------------------------
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('index.html')


@main.route('/hello')
def publish_hello():
    sse.publish({"user": "alice", "status": "Life is good!"}, channel="users.social", type='greeting')
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"
