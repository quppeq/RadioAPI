from flask import current_app, jsonify, request, abort, g, render_template, make_response, redirect, url_for
from flask.views import MethodView
from db import db
from radio.models.user import User
import logging

log = logging.getLogger(__name__)


class LoginView(MethodView):

    def get(self):
        return render_template('login/index.jinja')

    def post(self):
        token = request.form['token']
        from radio.models.user import User
        from db import db

        user = db.session.query(User).filter(
            User.session_token == token
        ).first()
        if user:
            response = make_response(redirect(url_for('.RadioView')))
            response.set_cookie('Authorization', token)
            return response

        return render_template('login/index.jinja')

class LogoutView(MethodView):

    def get(self):
        response = make_response(redirect(url_for('.RadioView')))
        response.set_cookie('Authorization', '', expires=0)
        return response
