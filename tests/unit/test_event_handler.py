import pytest

from google_hangouts_chat_bot.commands import Commands
from google_hangouts_chat_bot.event_handler import EventHandler
from tests.unit.helpers import NotImplementedCommand
from tests.unit.commands.Hidden import Hidden
from tests.unit.commands.Hello import Hello
from tests.unit.commands.Ciao import Ciao


def test_event_handler_with_none_payload():
    with pytest.raises(TypeError):
        EventHandler(None, Commands())


def test_event_handler_with_empty_payload():
    with pytest.raises(ValueError):
        EventHandler({}, Commands())


def test_event_handler_non_empty_without_type():
    with pytest.raises(ValueError):
        EventHandler({"foo": "bar"}, Commands())


def test_event_handler_with_invalid_type():
    with pytest.raises(ValueError):
        EventHandler(
            {"type": "INVALID_TYPE", "space": "", "user": ""}, Commands()
        ).process()


def test_event_handler_with_invalid_commands():
    payload = {"type": "", "space": "", "user": ""}

    with pytest.raises(TypeError):
        EventHandler(payload, None)


def test_event_handler_help_with_one_command():
    payload = {
        "type": "MESSAGE",
        "message": {"text": "help", "sender": {}},
        "space": "",
        "user": "",
    }

    commands = Commands()
    commands.add_command(Ciao)

    expected = {
        "text": "Commands available:\n\n"
        "*`ciao`*\nSay ciao\n\n"
        "*`help`*\nList commands available\n\n"
        'HINT: If you need to specify multiple words for a parameter, use quotes (").'
    }

    assert EventHandler(payload, commands).process() == expected


def test_event_handler_help_with_multiple_commands():
    payload = {
        "type": "MESSAGE",
        "message": {"text": "help", "sender": {}},
        "space": "",
        "user": "",
    }

    commands = Commands()
    commands.add_command(Ciao)
    commands.add_command(Hello)

    expected = {
        "text": "Commands available:\n\n"
        "*`ciao`*\nSay ciao\n\n"
        "*`hello`*`<name>`\nSay hello\n\n"
        "*`help`*\nList commands available\n\n"
        'HINT: If you need to specify multiple words for a parameter, use quotes (").'
    }

    assert EventHandler(payload, commands).process() == expected


def test_event_handler_help_with_hidden_command():
    payload = {
        "type": "MESSAGE",
        "message": {"text": "help", "sender": {}},
        "space": "",
        "user": "",
    }

    commands = Commands()
    commands.add_command(Ciao)
    commands.add_command(Hidden)

    expected = {
        "text": "Commands available:\n\n"
        "*`ciao`*\nSay ciao\n\n"
        "*`help`*\nList commands available\n\n"
        'HINT: If you need to specify multiple words for a parameter, use quotes (").'
    }

    assert EventHandler(payload, commands).process() == expected


def test_event_handler_with_unimplemented_command():
    payload = {
        "type": "MESSAGE",
        "message": {"text": "not-implemented-command", "sender": {}},
        "space": "",
        "user": "",
    }

    commands = Commands()
    commands.add_command(NotImplementedCommand)

    expected = {"text": "Oops, something went wrong!"}

    assert EventHandler(payload, commands).process() == expected


def test_event_handler_hello():
    payload = {
        "type": "MESSAGE",
        "message": {"text": "hello Jean", "sender": {}},
        "space": "",
        "user": "",
    }

    commands = Commands()
    commands.add_command(Hello)

    expected = {"text": "Hello, Jean!"}

    assert EventHandler(payload, commands).process() == expected
