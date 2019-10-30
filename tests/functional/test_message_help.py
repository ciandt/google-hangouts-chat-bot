from google_hangouts_chat_bot.commands import Commands
from google_hangouts_chat_bot.event_handler import EventHandler
from tests.functional.helpers import load_payload


def test_message_help():
    payload = load_payload("message_help")

    expected = {
        "text": "Commands available:\n\n"
        "*`help`*\nList commands available\n\n"
        'HINT: If you need to specify multiple words for a parameter, use quotes (").'
    }

    assert EventHandler(payload, Commands()).process() == expected
