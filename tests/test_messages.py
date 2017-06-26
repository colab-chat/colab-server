import env
import pytest
from datetime import datetime
from web.colab_server.messages.message import Message, MessageType
from web.colab_server.messages.message_text import TextMessage
from web.colab_server.messages.message_image import ImageMessage


class MockMessage(Message):
    def __init__(self, author, last_author, time_created, time_last_modified,
                 topic, message):
        super(MockMessage, self).__init__(
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
    MockMessage('test_author', 'last_test_author', datetime.now(),
                datetime.now(), 'message test string', 'test_topic')


def test_message_non_string_author_fails():
    author = 42
    with pytest.raises(ValueError):
        MockMessage(author, 'last_test_author', datetime.now(),
                    datetime.now(), 'message test string', 'test_topic')


def test_message_get_author():
    author = 'test_author'
    message = MockMessage(author, 'last_test_author', datetime.now(),
                          datetime.now(), 'message test string', 'test_topic')
    assert message.get_author() == author


def test_message_non_string_last_author_fails():
    last_author = 42
    with pytest.raises(ValueError):
        MockMessage('test_author', last_author, datetime.now(),
                    datetime.now(), 'message test string', 'test_topic')


def test_message_get_last_author():
    last_author = 'last_test_author'
    message = MockMessage('test_author', last_author, datetime.now(),
                          datetime.now(), 'message test string', 'test_topic')
    assert message.get_last_author() == last_author
