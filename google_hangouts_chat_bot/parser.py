import shlex


def parse(message):
    if "text" not in message:
        raise ValueError("Invalid message data")

    text = message["text"]

    if "annotations" in message:
        annotations = message["annotations"]

        for annotation in annotations:
            if annotation["type"] != "USER_MENTION":
                continue

            name = "@" + annotation["userMention"]["user"].get("displayName", "")
            email = annotation["userMention"]["user"].get("email", "")
            text = text.replace(name, email, 1)

    return shlex.split(text.strip())


def parse_action(action):
    if "actionMethodName" not in action:
        raise ValueError("Invalid action data")

    return shlex.split(action["actionMethodName"].strip())
