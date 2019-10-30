from google_hangouts_chat_bot.commands import Commands
from google_hangouts_chat_bot.event_handler import EventHandler
from tests.functional.helpers import load_payload


def test_message_simple_mention_on_room():
    payload = load_payload("message_simple_mention_on_room")

    expected = {"text": "pong"}

    assert EventHandler(payload, Commands()).process() == expected
