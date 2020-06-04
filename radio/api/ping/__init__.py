from flask import current_app, jsonify
from flask.views import MethodView
from db import db
from radio.models.radio import Track

class Version(MethodView):

    def get(self):
        db.session.query(Track).all()
        version = (current_app.config["VERSION"])
        response = {'version': version}
        return jsonify(response)
