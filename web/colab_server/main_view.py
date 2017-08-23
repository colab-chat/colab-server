from flask import Blueprint, render_template, current_app
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
    current_app.logger.warning('Hit index')
    return render_template('index.html')


@main.route('/hello')
def publish_hello():
    sse.publish(
        TextMessage('author', 'last_author', datetime.now(), datetime.now(),
                    'Life is good!', 'test_avro_topic'))
    return "Message sent!"
