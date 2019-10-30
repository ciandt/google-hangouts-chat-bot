from collections import OrderedDict

import pytest

from google_hangouts_chat_bot.commands import Commands, Ping, Help
from tests.unit.commands.Ciao import Ciao
from tests.unit.commands.Hello import Hello
from tests.unit.helpers import Invalid, WithoutCommand


def test_add_command_none():
    commands = Commands()
    with pytest.raises(TypeError):
        commands.add_command(None)


def test_add_command_invalid_class():
    commands = Commands()
    with pytest.raises(TypeError):
        commands.add_command(Invalid)


def test_add_command_incomplete_class():
    commands = Commands()
    with pytest.raises(TypeError):
        commands.add_command(WithoutCommand)


def test_add_command():
    commands = Commands()
    commands.add_command(Ciao)

    expected = OrderedDict(ciao=Ciao, ping=Ping, help=Help)
    assert commands.get_commands() == expected


def test_add_command_with_alias():
    commands = Commands()
    commands.add_command(Hello)

    expected = OrderedDict(hello=Hello, hi=Hello, hey=Hello, ping=Ping, help=Help)
    assert commands.get_commands() == expected


def test_add_commands():
    commands = Commands()
    commands.add_command(Hello)
    commands.add_command(Ciao)

    expected = OrderedDict(
        hello=Hello, hi=Hello, hey=Hello, ciao=Ciao, ping=Ping, help=Help
    )
    assert commands.get_commands() == expected


def test_add_command_from_module_none():
    commands = Commands()
    with pytest.raises(TypeError):
        commands.add_commands_from_module(None)


def test_add_command_from_module():
    commands = Commands()

    import tests.unit.commands

    commands.add_commands_from_module(tests.unit.commands)
