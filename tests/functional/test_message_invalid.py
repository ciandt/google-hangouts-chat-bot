from google_hangouts_chat_bot.commands import Commands
from google_hangouts_chat_bot.event_handler import EventHandler
from tests.functional.helpers import load_payload


def test_message_invalid():
    payload = load_payload("message_invalid")

    expected = {
        "text": "Invalid command: *invalid*\n\nPlease, type *help* for more information about the commands available."
    }

    assert EventHandler(payload, Commands()).process() == expected
