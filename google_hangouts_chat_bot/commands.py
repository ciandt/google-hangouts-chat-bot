import importlib
import inspect
import pkgutil
import types
from collections import OrderedDict
from copy import copy

from google_hangouts_chat_bot.responses import create_text_response


class Command:
    command = None
    command_aliases = []
    arguments = None
    description = None
    hidden = False

    def handle(self, arguments, **kwargs):
        raise NotImplementedError


class Commands:
    def __init__(self):
        self._commands = OrderedDict()

    def add_command(self, command):
        self._add_command(self._commands, command)

    @staticmethod
    def _add_command(container, command):
        if not inspect.isclass(command) or not issubclass(command, Command):
            raise TypeError("command must derive from Command class")

        if not command.command:
            raise TypeError("Invalid command")

        container[command.command] = command

        if isinstance(command.command_aliases, list):
            for command_alias in command.command_aliases:
                container[command_alias] = command

    def add_commands_from_module(self, module):
        if not isinstance(module, types.ModuleType):
            raise TypeError("Invalid module")

        for _, name, _ in pkgutil.walk_packages(module.__path__, module.__name__ + "."):
            imported_module = importlib.import_module(name)

            # we only want classes defined in this module
            for _, klass in inspect.getmembers(imported_module, inspect.isclass):
                if module.__name__ in klass.__module__:
                    self.add_command(klass)

    def get_commands(self):

        copied = copy(self._commands)

        self._add_command(copied, Ping)
        self._add_command(copied, Help)

        return copied


# Built-in commands
class Ping(Command):
    command = "ping"
    description = "Ping"
    hidden = True

    def handle(self, arguments, **kwargs):
        return create_text_response("pong")


class Help(Command):
    command = "help"
    description = "List commands available"

    def handle(self, arguments, **kwargs):
        text = [
            "Commands available:",
            "",
        ]

        for key, command in kwargs.pop("commands", OrderedDict()).items():
            if command.hidden:
                continue

            if key != command.command:
                # must be an alias
                continue

            if command.arguments:
                text.append(
                    f"*`{command.command}`*`{command.arguments}`\n{command.description}\n"
                )
            else:
                text.append(f"*`{command.command}`*\n{command.description}\n")

        text.append(
            'HINT: If you need to specify multiple words for a parameter, use quotes (").'
        )

        return create_text_response("\n".join(text))
