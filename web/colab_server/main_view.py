from flask import Blueprint, render_template
from flask_user import login_required
from .flask_sse_kafka import sse
from .messages.message_text import TextMessage
from datetime import datetime

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
    # sse.publish({"user": "alice", "status": "Life is good!"}, channel="users.social", type='greeting')
    sse.publish(
        TextMessage('author', 'last_author', datetime.now(), datetime.now(), 'test_avro_topic', 'Life is good!'),
        type='greeting')
    return "Message sent!"
