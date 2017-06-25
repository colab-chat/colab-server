from fastavro import writer
import io
import uuid
from .avroschema import schema, event_schema


class AvroSerialiser:
    def __init__(self):
        pass

    @staticmethod
    def serialise_message(message):
        buffer = io.BytesIO()
        writer(buffer, schema, [{'id': uuid.uuid4().int,
                                 'author': message.get_author(),
                                 'type': message.get_message_type().value,
                                 'raw_text': message.get_raw_message(),
                                 'timestamp': message.get_time_created().timestamp(),
                                 'topic': message.get_topic(),
                                 'html': message.get_html()}])
        return buffer.getvalue()

    @staticmethod
    def serialize_binary_message(message):
        buffer = io.BytesIO()
        writer(buffer, schema, [{'id': uuid.uuid4().int,
                                 'author': message.get_author(),
                                 'type': message.get_message_type().value,
                                 'binary': message.get_raw_message(),
                                 'timestamp': message.get_time_created().timestamp(),
                                 'topic': message.get_topic(),
                                 'html': message.get_html()}])
        return buffer.getvalue()

    @staticmethod
    def serialise_event_message(event_type, name):
        buffer = io.BytesIO()
        writer(buffer, event_schema, [{'event_type': event_type, 'name': name}])
        return buffer.getvalue()
