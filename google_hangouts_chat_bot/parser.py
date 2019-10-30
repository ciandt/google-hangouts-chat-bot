import shlex


def parse(message):
    if not "text" in message:
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
