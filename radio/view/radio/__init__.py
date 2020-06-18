from flask import current_app, jsonify, request, abort, g, render_template
from flask.views import MethodView
from db import db
from radio.models.user import User
import logging
from datetime import datetime
from dateutil import relativedelta

log = logging.getLogger(__name__)


class RadioView(MethodView):

    def get(self):

        return render_template('radio/index.jinja')
