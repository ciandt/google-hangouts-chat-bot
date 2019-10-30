from google_hangouts_chat_bot.commands import Command
from google_hangouts_chat_bot.responses import create_text_response


class Ciao(Command):
    command = "ciao"
    description = "Say ciao"

    def handle(self, arguments, **kwargs):
        return create_text_response("Ciao!")
