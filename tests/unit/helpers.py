from google_hangouts_chat_bot.commands import Command
from google_hangouts_chat_bot.responses import create_text_response


class Invalid:
    pass


class WithoutCommand(Command):
    def handle(self, arguments, **kwargs):
        pass


class NotImplementedCommand(Command):
    command = "not-implemented-command"


class DependencyInjection(Command):
    command = "dependency"
    description = "Test dependency injection"
    hidden = True

    def handle(self, arguments, **kwargs):
        return create_text_response(f"Repository = {kwargs['repository']}")
