from flask import current_app, jsonify, request, abort
from flask.views import MethodView
from db import db
from radio.models.user import User
import logging
log = logging.getLogger(__name__)


class LoginView(MethodView):

    def post(self):
        data = request.json
        if not isinstance(data, dict):
            abort(400)
        tg_id = data.get('telegram_id')
        name = data.get('name')

        # TODO: Зробити нормальну валідацію що логін йде з кормального місця
        secret = data.get('secret_key')
        if secret != 'telegram_bot':
            log.warning(f'bad login for id: {tg_id}')
            abort(403)


        user = db.session.query(User).filter(
            User.telegram_id == tg_id
        ).first
        if not user:
            user = User(telegram_id=tg_id, name=name)
            db.session.add(user)

        session_token = "random_token"
        user.session_token = session_token

        db.session.commit()

        log.info(f'Successful login for {user.name}. Telegram id: {user.telegram_id}')
        response = dict(session_token=session_token)
        return jsonify(response)