from flask import request, current_app, abort, g
from functools import wraps
from db import db
from radio.models.user import User, Role


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):

        if not request.json or 'Authorization' not in request.json:
           abort(401)

        token = str(request.json['Authorization'])
        user = db.session.query(User, User.session_token == token).first()
        if not user:
            abort(401)
        g.user = user
        return f(*args, **kws)

    return decorated_function
