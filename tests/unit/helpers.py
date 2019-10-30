from google_hangouts_chat_bot.commands import Command


class Invalid:
    pass


class WithoutCommand(Command):
    def handle(self, arguments, **kwargs):
        pass


class NotImplementedCommand(Command):
    command = "not-implemented-command"
