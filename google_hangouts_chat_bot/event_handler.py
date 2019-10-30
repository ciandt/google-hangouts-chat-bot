import logging

from google_hangouts_chat_bot.commands import Commands
from google_hangouts_chat_bot.parser import parse
from google_hangouts_chat_bot.responses import create_text_response


class EventHandler:
    def __init__(self, payload, commands):
        if not isinstance(payload, dict):
            raise TypeError("Invalid payload")

        if (
            len(payload) == 0
            or "type" not in payload
            or "space" not in payload
            or "user" not in payload
        ):
            raise ValueError("Invalid payload")

        if not isinstance(commands, Commands):
            raise TypeError("Invalid commands. Must be a Commands class")

        self._payload = payload
        self._commands = commands.get_commands()

    def process(self):

        event_type = self._payload["type"]

        if event_type == "ADDED_TO_SPACE":
            return self._on_added_to_space()

        if event_type == "REMOVED_FROM_SPACE":
            return self._on_removed_from_space()

        if event_type == "MESSAGE":
            return self._on_message()

        raise ValueError(f"Invalid event type: {event_type}")

    def _on_added_to_space(self):
        space = self._payload["space"]
        user = self._payload["user"]

        logging.info("Bot added to space: %s", space)

        text = ""

        if space["type"] == "ROOM":
            text = f'Hello people! Thanks for adding me to *{space["displayName"]}*!'

        elif space["type"] == "DM":
            text = f'Hello <{user["name"]}>! How are you?'

        text += (
            "\n\nPlease, type *help* for more information about the commands available."
        )

        return create_text_response(text)

    def _on_removed_from_space(self):
        space = self._payload["space"]
        logging.info("Bot removed from space: %s", space)

    def _on_message(self):
        args = parse(self._payload["message"])
        sender = self._payload["message"]["sender"]

        logging.info("Args parsed: %s", args)

        if len(args) == 0:
            args = ["help"]

        command = args.pop(0).lower()

        if command not in self._commands:
            return self._invalid_command(command)

        try:
            klass = self._commands.get(command)
            return klass().handle(args, sender=sender, commands=self._commands)
        except Exception as exc:
            logging.exception(exc)
            return create_text_response("Oops, something went wrong!")

    @staticmethod
    def _invalid_command(command):
        text = [
            f"Invalid command: *{command}*",
            "",
            "Please, type *help* for more information about the commands available.",
        ]

        return create_text_response("\n".join(text))
