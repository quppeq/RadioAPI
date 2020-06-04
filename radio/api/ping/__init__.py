from flask import current_app, jsonify
from flask.views import MethodView


class Version(MethodView):

    def get(self):
        version = (current_app.config["VERSION"])
        response = {'version': version}
        return jsonify(response)
