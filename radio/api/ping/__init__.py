from flask import current_app, jsonify, g
from flask.views import MethodView
from db import db
from radio.models.radio import Track
from radio.lib.decorators import authorize

class VersionView(MethodView):

    def get(self):
        version = (current_app.config["VERSION"])
        response = {'version': version}
        return jsonify(response)

    @authorize
    def post(self):
        version = (current_app.config["VERSION"])
        response = {'version': version}
        print(g.user)
        return jsonify(response)
