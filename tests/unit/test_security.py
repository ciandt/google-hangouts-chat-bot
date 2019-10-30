from unittest import mock

import pytest

from google_hangouts_chat_bot.security import (
    check_allowed_domain,
    check_bot_authenticity,
)


def test_check_allowed_domain_with_invalid_domains():
    with pytest.raises(TypeError):
        check_allowed_domain("jean@email.com", None)


def test_check_allowed_domain_with_empty_domains():
    with pytest.raises(ValueError):
        check_allowed_domain("jean@email.com", [])

    with pytest.raises(ValueError):
        check_allowed_domain("jean@email.com", [None, None])


def test_check_allowed_domain_with_no_email():
    allowed_domains = ["ciandt.com", "google.com"]

    with pytest.raises(ValueError):
        check_allowed_domain(None, allowed_domains)

    with pytest.raises(ValueError):
        check_allowed_domain("", allowed_domains)

    with pytest.raises(ValueError):
        check_allowed_domain("not-an-email", allowed_domains)


def test_check_allowed_domain():
    check_allowed_domain("allowed@ciandt.com", ["ciandt.com", "google.com"])


def test_check_disallowed_domain():
    with pytest.raises(ValueError):
        check_allowed_domain("disallowed@server.com", ["ciandt.com", "google.com"])


def test_check_bot_authenticity_with_invalid_params():
    with pytest.raises(ValueError):
        check_bot_authenticity(None, "123456")

    with pytest.raises(ValueError):
        check_bot_authenticity("token", None)


def test_check_bot_authenticity_with_invalid_token():
    with mock.patch(
        "google.oauth2.id_token.verify_token", return_value={"iss": "server.com"}
    ) as verify_token:
        with pytest.raises(ValueError):
            check_bot_authenticity("any token", "123456")

        verify_token.assert_called_once()


def test_check_bot_authenticity():
    with mock.patch(
        "google.oauth2.id_token.verify_token",
        return_value={"iss": "chat@system.gserviceaccount.com"},
    ) as verify_token:
        check_bot_authenticity("any token", "123456")

        verify_token.assert_called_once()
