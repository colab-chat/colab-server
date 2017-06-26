from .avroschema import schema, event_schema
from fastavro import reader
import io
from ..messages.message import MessageType
from ..messages.message_text import TextMessage
from ..messages.message_image import ImageMessage
from datetime import datetime


class AvroDeserialiser:
    def __init__(self):
        pass

    @staticmethod
    def deserialise(buffer):
        output = reader(io.BytesIO(buffer), schema)
        new_message = None
        for message in output:
            if MessageType(message['type']) is MessageType.TEXT:
                new_message = TextMessage(message['author'], 'last_author',
                                          datetime.fromtimestamp(
                                              message['timestamp']),
                                          datetime.fromtimestamp(0),
                                          message['topic'],
                                          message['raw_text'])
            elif MessageType(message['type']) is MessageType.IMAGE:
                new_message = ImageMessage(message['author'], 'last_author',
                                           datetime.fromtimestamp(
                                               message['timestamp']),
                                           datetime.fromtimestamp(0),
                                           message['binary'], message['topic'],
                                           html=message['html'])
            else:
                raise ValueError(
                    'Unrecognised message type in AvroSerialise.deserialise')
        return new_message

    def deserialise_event_message(self, buffer):
        output = reader(io.BytesIO(buffer), event_schema)
        event_type = None
        name = None
        for message in output:
            event_type = message['event_type']
            name = message['name']
        return event_type, name
