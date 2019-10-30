from google_hangouts_chat_bot.commands import Command
from google_hangouts_chat_bot.responses import create_text_response


class Hidden(Command):
    command = "hidden"
    description = "Hidden commands should not be listed"
    hidden = True

    def handle(self, arguments, **kwargs):
        return create_text_response("Hello!")
