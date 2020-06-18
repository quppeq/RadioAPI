from flask import current_app, jsonify, request, abort, g, render_template
from flask.views import MethodView
from db import db
from radio.models.user import User
from radio.lib.radio import get_now
from radio.lib.decorators import authorize
import logging

log = logging.getLogger(__name__)


class RadioView(MethodView):

    def get(self):
        now = get_now()

        return render_template('radio/index.jinja', radio_src="http://127.0.0.1:8000/radio.ogg", now=now)


class RadioHistoryView(MethodView):

    @authorize
    def get(self):
        return ""