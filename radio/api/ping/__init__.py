from flask import current_app, jsonify
from flask.views import MethodView

class Ping(MethodView):

    def get(self):
        version = (current_app.config["VERSION"])
        return jsonify(version)
