import pytest

from google_hangouts_chat_bot.parser import parse


def test_invalid_payload():
    with pytest.raises(ValueError):
        parse({})


def test_invalid_key_payload():
    with pytest.raises(ValueError):
        parse({"txt": None})


def test_simple_payload():
    args = parse({"text": "Hello"})

    assert args == ["Hello"]


def test_spaced_payload():
    args = parse({"text": "Hello World"})

    assert args == ["Hello", "World"]


def test_simple_quoted_payload():
    args = parse({"text": '"Hello World"'})

    assert args == ["Hello World"]


def test_quoted_payload():
    args = parse({"text": 'Hi! "Hello World"'})

    assert args == ["Hi!", "Hello World"]


def test_mention_without_annotations_payload():
    args = parse({"text": "@Tech Gallery hello world"})

    assert args == ["@Tech", "Gallery", "hello", "world"]


def test_invalid_mention_payload():
    args = parse(
        {
            "text": "@Tech Gallery hello world",
            "annotations": [
                {
                    "type": "INVALID_TYPE",
                    "startIndex": 0,
                    "length": 13,
                    "userMention": {
                        "user": {
                            "name": "users/123456",
                            "displayName": "Tech Gallery",
                            "avatarUrl": "https://lh3.googleusercontent.com/NjgynwOVAgrdI1",
                            "type": "BOT",
                        },
                        "type": "MENTION",
                    },
                }
            ],
        }
    )

    assert args == ["@Tech", "Gallery", "hello", "world"]


def test_bot_mention_payload():
    args = parse(
        {
            "text": "@Tech Gallery hello world",
            "annotations": [
                {
                    "type": "USER_MENTION",
                    "startIndex": 0,
                    "length": 13,
                    "userMention": {
                        "user": {
                            "name": "users/123456",
                            "displayName": "Tech Gallery",
                            "avatarUrl": "https://lh3.googleusercontent.com/NjgynwOVAgrdI1",
                            "type": "BOT",
                        },
                        "type": "MENTION",
                    },
                }
            ],
        }
    )

    assert args == ["hello", "world"]


def test_more_mentions_payload():
    args = parse(
        {
            "text": "@Tech Gallery hello @Jean Pimentel",
            "annotations": [
                {
                    "type": "USER_MENTION",
                    "startIndex": 0,
                    "length": 13,
                    "userMention": {
                        "user": {
                            "name": "users/123456",
                            "displayName": "Tech Gallery",
                            "avatarUrl": "https://lh3.googleusercontent.com/NjgynwOVAgrdI1",
                            "type": "BOT",
                        },
                        "type": "MENTION",
                    },
                },
                {
                    "type": "USER_MENTION",
                    "startIndex": 20,
                    "length": 14,
                    "userMention": {
                        "user": {
                            "name": "users/123789",
                            "displayName": "Jean Pimentel",
                            "avatarUrl": "https://lh3.googleusercontent.com/a-/AAstDdyXmUsl2w",
                            "email": "jpimentel@ciandt.com",
                            "type": "HUMAN",
                        },
                        "type": "MENTION",
                    },
                },
            ],
        }
    )

    assert args == ["hello", "jpimentel@ciandt.com"]
