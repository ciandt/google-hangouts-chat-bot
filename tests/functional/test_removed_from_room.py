from google_hangouts_chat_bot.commands import Commands
from google_hangouts_chat_bot.event_handler import EventHandler
from tests.functional.helpers import load_payload


def test_removed_from_room():
    payload = load_payload("removed_from_room")
    EventHandler(payload, Commands()).process()
