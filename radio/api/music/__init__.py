from flask import current_app, jsonify
from flask.views import MethodView
from db import db
from radio.models.radio import Track


class TrackView(MethodView):

    def get(self, track_id: int):
        track = db.session.query(Track).filter(
            Track.id == track_id
        ).first()
        response = dict(
            id=track.id,
            name=track.name,
        ) if track else {}
        return jsonify(response)


class MusicListView(MethodView):

    def get(self):
        tracks = db.session.query(Track).all()
        response = [dict(
            id=track.id,
            name=track.name,
        ) for track in tracks]

        return jsonify(response)
