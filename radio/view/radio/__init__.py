from flask import current_app, jsonify, request, abort, g, render_template
from flask.views import MethodView
from db import db
from sqlalchemy import func
from radio.models.user import User
from radio.models.radio import Queue, Track, PartOfDayEnum
from radio.lib.radio import get_now
from radio.lib.decorators import authorize
import logging
from datetime import datetime

log = logging.getLogger(__name__)


class RadioView(MethodView):

    def get(self):
        now = get_now()

        return render_template('radio/index.jinja', radio_src="http://127.0.0.1:8000/radio.ogg", now=now)


class RadioHistoryView(MethodView):

    @authorize
    def get(self):
        today = datetime.now().date()
        morning = db.session.query(Queue).filter(
            Queue.part == PartOfDayEnum.morning.value,
            Queue.day == today,
        ).all()

        afternoon = db.session.query(Queue).filter(
            Queue.part == PartOfDayEnum.afternoon.value,
            Queue.day == today,
        ).all()

        evening = db.session.query(Queue).filter(
            Queue.part == PartOfDayEnum.evening.value,
            Queue.day == today,
        ).all()

        return render_template('radio/history.jinja', morning=morning, afternoon=afternoon, evening=evening)