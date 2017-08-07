from flask import Blueprint, current_app, json, stream_with_context
from .streaming.avroserialiser import AvroSerialiser
from .streaming.avrodeserialiser import AvroDeserialiser
from .messages.message import Message
from confluent_kafka import Producer, Consumer, KafkaError
from time import sleep

KAFKA_BROKER = 'kafka'
TOPIC_NAME = 'another_topic'
serialiser = AvroSerialiser()
deserialiser = AvroDeserialiser()


def delivery_callback(err, msg):
    if err:
        current_app.logger.error('%% Message failed delivery: %s\n' % err)
    else:
        current_app.logger.error('%% Message delivered to %s [%d]\n' %
                                 (msg.topic(), msg.partition()))


class ServerSentEventsBlueprint(Blueprint):
    """
    A :class:`flask.Blueprint` subclass that knows how to publish,
    subscribe to, and stream server-sent events.
    """
    producer = Producer({'bootstrap.servers': KAFKA_BROKER})

    consumer = Consumer({'bootstrap.servers': KAFKA_BROKER, 'group.id': None,
                         'default.topic.config': {
                             'auto.offset.reset': 'largest',
                             'enable.auto.commit': 'false'}})

    def publish(self, message, channel=TOPIC_NAME):
        """
        Publish data as a server-sent event.
        :param message: The message to send.
        :param channel: If you want to direct different events to different
            clients, you may specify a channel for this event to go to.
            Only clients listening to the same channel will receive this event.
            Each channel will map to a Kafka topic with the same name.
            Defaults to "test_avro_topic".
        """
        assert (isinstance(message, Message))
        current_app.logger.debug(
            'ServerSentEventsBlueprint.publish: publishing message to kafka')
        try:
            self.producer.produce(channel, message.serialize(),
                                  callback=delivery_callback)
        except BufferError as e:
            current_app.logger.error(
                '%% Local producer queue is full (%d messages waiting)\n' %
                len(self.producer))
        self.producer.poll(0)

    def messages(self):
        """
        A generator of ...
        """
        current_app.logger.debug("in ServerSentEventsBlueprint.messages")
        self.consumer.subscribe([TOPIC_NAME])
        running = True
        while running:
            try:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    sleep(0.05)
                    continue
                if not msg.error():
                    message = deserialiser.deserialise(msg.value())
                    current_app.logger.debug(message.get_html())
                    payload = {'message': message.get_html(),
                               'name': message.get_author(),
                               'topic': message.get_topic(),
                               'raw_message': message.get_raw_message(),
                               'message_type': message.get_message_type(),
                               'time_created': message.get_time_created(),
                               }
                    yield json.dumps(payload)
                elif msg.error().code() != KafkaError._PARTITION_EOF:
                    current_app.logger.error(msg.error())
            except:
                current_app.logger.error('error polling consumer')

    def stream(self):
        """
        A view function that streams server-sent events. Ignores any
        :mailheader:`Last-Event-ID` headers in the HTTP request.
        """
        current_app.logger.debug('in ServerSentEventsBlueprint.stream')

        @stream_with_context
        def generator():
            for message in self.messages():
                lines = ["data:{value}".format(value=line) for line in
                         message.splitlines()]
                lines.insert(0, "event:{value}".format(value='message'))
                yield "\n".join(lines) + "\n\n"

        return current_app.response_class(
            generator(),
            mimetype='text/event-stream',
        )


sse = ServerSentEventsBlueprint('sse', __name__)
"""
An instance of :class:`~flask_sse.ServerSentEventsBlueprint`
that hooks up the :meth:`~flask_sse.ServerSentEventsBlueprint.stream`
method as a view function at the root of the blueprint. If you don't
want to customize this blueprint at all, you can simply import and
use this instance in your application.
"""
sse.add_url_rule(rule="", endpoint="stream", view_func=sse.stream)
