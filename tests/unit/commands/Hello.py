from google_hangouts_chat_bot.commands import Command
from google_hangouts_chat_bot.responses import create_text_response


class Hello(Command):
    command = "hello"
    command_aliases = ["hi", "hey"]
    arguments = "<name>"
    description = "Say hello"

    def handle(self, arguments, **kwargs):
        return create_text_response(f"Hello, {arguments[0]}!")
