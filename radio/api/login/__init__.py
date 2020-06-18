from flask import current_app, jsonify, request, abort, g
from flask.views import MethodView
from db import db
from radio.models.user import User
import logging
from datetime import datetime
from dateutil import relativedelta

from .helpers import generator_token
log = logging.getLogger(__name__)


class LoginView(MethodView):

    def post(self):
        SECRET_KEY = current_app.config["BOT_SHARED_SECRET"]

        data = request.json
        if not isinstance(data, dict):
            abort(400)
        tg_id = data.get('telegram_id')
        name = data.get('name')
        if not (tg_id and name):
            abort(400)

        # TODO: Зробити нормальну валідацію що логін йде з нормального місця
        secret = data.get('secret_key')
        if secret != SECRET_KEY:
            log.warning(f'bad login for id: {tg_id}')
            abort(403)

        user = db.session.query(User).filter(
            User.telegram_id == tg_id
        ).first()
        if not user:
            user = User(telegram_id=tg_id, name=name)

            db.session.add(user)

        session_token = generator_token()

        user.session_token = session_token

        auth_time = datetime.now()

        #   Перевіряємо аби часто не логінились
        if user.last_auth and user.last_auth + relativedelta.relativedelta(minutes=30) > auth_time:
            abort(429)
        user.last_auth = auth_time

        db.session.commit()

        log.info(f'Successful login for {user.name}. Telegram id: {user.telegram_id}')
        response = dict(session_token=session_token)
        return jsonify(response)
