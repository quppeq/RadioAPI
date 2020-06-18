from flask import request, current_app, abort, g
from functools import wraps
from db import db
from radio.models.user import User, Role
from radio.lib.login import auth


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        _, user = auth()
        if not user:
            abort(401)
        return f(*args, **kws)

    return decorated_function
