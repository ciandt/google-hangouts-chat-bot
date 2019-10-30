from google_hangouts_chat_bot.commands import Commands
from google_hangouts_chat_bot.event_handler import EventHandler
from tests.functional.helpers import load_payload


def test_added_to_dm():
    payload = load_payload("added_to_dm")

    expected = {
        "text": "Hello <users/123456789123456789123>! How are you?\n\nPlease, type *help* for more information about the commands available."
    }

    assert EventHandler(payload, Commands()).process() == expected
