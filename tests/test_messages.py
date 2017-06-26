import env
import pytest
from datetime import datetime
from web.colab_server.messages.message import Message, MessageType
from web.colab_server.messages.message_text import TextMessage
from web.colab_server.messages.message_image import ImageMessage


class FakeMessage(Message):
    def __init__(self, author, last_author, time_created, time_last_modified,
                 topic, message):
        super(FakeMessage, self).__init__(
            author=author,
            last_author=last_author,
            time_created=time_created,
            time_last_modified=time_last_modified,
            topic=topic, message=message)
        self._message_type = MessageType.MOCK

    def serialize(self):
        pass

    def _do_create_html_message(self):
        pass


def test_message_creation():
    FakeMessage('test_author', 'last_test_author', datetime.now(),
                datetime.now(), 'test_topic', 'message test string')


def test_message_non_string_author_fails():
    author = 42
    with pytest.raises(ValueError):
        FakeMessage(author, 'last_test_author', datetime.now(),
                    datetime.now(), 'test_topic', 'message test string')


def test_message_get_author():
    author = 'test_author'
    message = FakeMessage(author, 'last_test_author', datetime.now(),
                          datetime.now(), 'test_topic', 'message test string')
    assert message.get_author() == author


def test_message_non_string_last_author_fails():
    last_author = 42
    with pytest.raises(ValueError):
        FakeMessage('test_author', last_author, datetime.now(),
                    datetime.now(), 'test_topic', 'message test string')


def test_message_get_last_author():
    last_author = 'last_test_author'
    message = FakeMessage('test_author', last_author, datetime.now(),
                          datetime.now(), 'test_topic', 'message test string')
    assert message.get_last_author() == last_author


def test_message_non_datetime_created_fails():
    time_created = 42
    with pytest.raises(ValueError):
        FakeMessage('test_author', 'test_last_author', time_created,
                    datetime.now(), 'test_topic', 'message test string')


def test_message_get_time_created():
    time_created = datetime.now()
    message = FakeMessage('test_author', 'test_last_author', time_created,
                          datetime.now(), 'test_topic', 'message test string')
    assert message.get_time_created() == time_created


def test_message_non_datetime_last_modified_fails():
    time_modified = 42
    with pytest.raises(ValueError):
        FakeMessage('test_author', 'test_last_author', datetime.now(),
                    time_modified, 'test_topic', 'message test string')


def test_message_get_time_modified():
    time_modified = datetime.now()
    message = FakeMessage('test_author', 'test_last_author', datetime.now(),
                          time_modified, 'test_topic', 'message test string')
    assert message.get_time_last_modified() == time_modified


def test_message_get_message():
    message_contents = 'message test string'
    message = FakeMessage('test_author', 'test_last_author', datetime.now(),
                          datetime.now(), 'test_topic', message_contents)
    assert message.get_raw_message() == message_contents


def test_message_get_topic():
    topic = 'test_topic'
    message = FakeMessage('test_author', 'test_last_author', datetime.now(),
                          datetime.now(), topic, 'message test string')
    assert message.get_topic() == topic

