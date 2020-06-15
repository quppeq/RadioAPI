from os import urandom
from base64 import b64encode


def generator_token(length=18):
    res = urandom(length)
    return b64encode(res).decode()
