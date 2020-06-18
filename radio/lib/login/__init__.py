from flask import request, g
from db import db
from radio.models.user import User


def auth():
    token = None
    if request.json and 'Authorization' in request.json:
        token = str(request.json['Authorization'])
    elif 'Authorization' in request.cookies:
        token = request.cookies['Authorization']

    if not token:
        return False, None

    user = db.session.query(User).filter(
        User.session_token == token
    ).first()
    if not user:
        return False, None
    return True, user


def is_login():
    is_log, user = auth()
    return is_log


def g_login():
    is_log, user = auth()
    g.user = user
