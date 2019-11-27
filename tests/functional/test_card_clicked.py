from google_hangouts_chat_bot.commands import Commands
from google_hangouts_chat_bot.event_handler import EventHandler
from tests.functional.helpers import load_payload


def test_card_clicked():
    payload = load_payload("card_clicked")

    expected = {"text": "pong"}

    assert EventHandler(payload, Commands()).process() == expected
