from flask import Blueprint, request, current_app, json, stream_with_context
from kafka import KafkaConsumer
from kafka import KafkaProducer
from .streaming.avroserialiser import AvroSerialiser
from .streaming.avrodeserialiser import AvroDeserialiser
from .messages.message import Message

KAFKA_BROKER = '192.168.99.100'
serialiser = AvroSerialiser()
deserialiser = AvroDeserialiser()


class ServerSentEventsBlueprint(Blueprint):
    """
    A :class:`flask.Blueprint` subclass that knows how to publish, subscribe to,
    and stream server-sent events.
    """

    @property
    def producer(self):
        """
        A :class:`kafka.KafkaProducer` instance
        """
        return KafkaProducer(bootstrap_servers=[KAFKA_BROKER])

    @property
    def consumer(self):
        """
        A :class:`kafka.KafkaConsumer` instance
        """
        return KafkaConsumer('test_avro_topic',
                             group_id=None,
                             bootstrap_servers=[KAFKA_BROKER],
                             auto_offset_reset='earliest',
                             enable_auto_commit=False)

    def publish(self, message, channel='test_avro_topic'):
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
        return self.producer.send(channel, message.serialize())

    def messages(self):
        """
        A generator of ...
        """
        # TODO need to manage which topics we are subscribed to
        partitions = self.consumer.poll(timeout_ms=100, max_records=50)
        if len(partitions) > 0:
            for p in partitions:
                for response in partitions[p]:
                    message = deserialiser.deserialise(response.value)
                    raw_message = message.get_raw_message()
                    if isinstance(raw_message, bytes):
                        raw_message = raw_message.decode('utf8')
                    raw_message = raw_message.replace("'", "&#39;")
                    payload = {'message': message.get_html(),
                               'author': message.get_author(),
                               'raw_message': raw_message,
                               'time_created': message.get_time_created().strftime("%H:%M:%S %B %d, %Y"),
                               'topic': message.get_topic(),
                               'message_type': message.get_message_type().value}

                    yield "data: %s\n\n" % json.dumps(payload)

    def stream(self):
        """
        A view function that streams server-sent events. Ignores any
        :mailheader:`Last-Event-ID` headers in the HTTP request.
        """
        @stream_with_context
        def generator():
            for message in self.messages():
                yield str(message)

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
