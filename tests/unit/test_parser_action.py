import pytest

from google_hangouts_chat_bot.parser import parse_action


def test_invalid_payload():
    with pytest.raises(ValueError):
        parse_action({})


def test_invalid_key_payload():
    with pytest.raises(ValueError):
        parse_action({"txt": None})


def test_simple_payload():
    args = parse_action({"actionMethodName": "hello"})

    assert args == ["hello"]


def test_spaced_payload():
    args = parse_action({"actionMethodName": "hello world"})

    assert args == ["hello", "world"]


def test_simple_quoted_payload():
    args = parse_action({"actionMethodName": '"hello world"'})

    assert args == ["hello world"]


def test_quoted_payload():
    args = parse_action({"actionMethodName": 'Hello "Jane Doe"'})

    assert args == ["Hello", "Jane Doe"]
