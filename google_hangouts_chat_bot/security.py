from google.auth.transport import requests
from google.oauth2 import id_token

# Bearer Tokens received by bots will always specify this issuer.
CHAT_ISSUER = "chat@system.gserviceaccount.com"

# Url to obtain the public certificate for the issuer.
PUBLIC_CERT_URL_PREFIX = "https://www.googleapis.com/service_accounts/v1/metadata/x509/"


def check_allowed_domain(email, allowed_domains):
    if not isinstance(allowed_domains, list):
        raise TypeError(f"Allowed domains should be a list")

    allowed_domains = list(filter(None, allowed_domains))
    if len(allowed_domains) == 0:
        raise ValueError(f"Allowed domains should not be empty")

    try:
        domain = email.split("@")[1].lower()
    except:
        raise ValueError("Not an email")

    if domain not in allowed_domains:
        raise ValueError("Domain not allowed")


def check_bot_authenticity(token, audience):
    if not token:
        raise ValueError("Invalid token")

    if not audience:
        raise ValueError(f"Invalid audience")

    id_info = id_token.verify_token(
        token,
        requests.Request(),
        audience=audience,
        certs_url=PUBLIC_CERT_URL_PREFIX + CHAT_ISSUER,
    )

    if id_info["iss"] != CHAT_ISSUER:
        raise ValueError("Wrong issuer")
