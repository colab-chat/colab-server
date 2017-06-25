from flask import Blueprint, render_template, current_app
from flask_user import login_required
from .flask_sse_kafka import sse
from .messages.message_text import TextMessage
from datetime import datetime
from confluent_kafka import Producer, Consumer, KafkaError
from time import sleep

# -------------------------------
# Main blueprint
# -------------------------------
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
@login_required
def index():
    # current_app.my_logger.info('making producer')
    # KAFKA_BROKER = 'kafka'
    # p = Producer({'bootstrap.servers': KAFKA_BROKER})
    # p.produce('view_test', 'blah blah message content'.encode('utf-8'))
    # #p.flush()
    # current_app.my_logger.info('hopefully published a mesg')
    #
    # sleep(3)
    #
    # current_app.my_logger.info('making consumer')
    # c = Consumer({'bootstrap.servers': KAFKA_BROKER, 'group.id': 'groupid',
    #               'default.topic.config': {'auto.offset.reset': 'smallest',
    #                                        'enable.auto.commit': 'false'}})
    # current_app.my_logger.info('subbing')
    # c.subscribe(['view_test'])
    #
    # current_app.my_logger.info('polling')
    # msg = c.poll()
    # if not msg.error():
    #     current_app.my_logger.info('Received message: %s' % msg.value().decode('utf-8'))
    # elif msg.error().code() != KafkaError._PARTITION_EOF:
    #     current_app.my_logger.error(msg.error())

    current_app.my_logger.warning('Hit index')
    return render_template('index.html')


@main.route('/hello')
def publish_hello():
    sse.publish(
        TextMessage('author', 'last_author', datetime.now(), datetime.now(), 'test_avro_topic', 'Life is good!'))
    return "Message sent!"
