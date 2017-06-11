from flask import Blueprint, render_template, current_app
from flask_user import login_required
from .flask_sse_kafka import sse
from .messages.message_text import TextMessage
from datetime import datetime
from kafka import KafkaProducer, KafkaConsumer
from time import sleep

# -------------------------------
# Main blueprint
# -------------------------------
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
@login_required
def index():
    current_app.my_logger.warning('Hit index')

    producer = KafkaProducer(bootstrap_servers=['kafka'])
    producer.send('temp_test', b'foo test message')

    sleep(5)

    consumer = KafkaConsumer('temp_test',
                             group_id=None,
                             bootstrap_servers=['kafka'],
                             auto_offset_reset='earliest',
                             enable_auto_commit=False)
    partitions = consumer.poll(timeout_ms=100, max_records=50)
    if len(partitions) > 0:
        for p in partitions:
            for response in partitions[p]:
                current_app.my_logger.info(response.value)

    return render_template('index.html')


@main.route('/hello')
def publish_hello():
    # sse.publish({"user": "alice", "status": "Life is good!"}, channel="users.social", type='greeting')
    sse.publish(
        TextMessage('author', 'last_author', datetime.now(), datetime.now(), 'test_avro_topic', 'Life is good!'),
        type='greeting')
    return "Message sent!"
