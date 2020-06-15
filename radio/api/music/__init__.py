from flask import current_app, jsonify, g, request
from flask.views import MethodView
from db import db
from radio.models.radio import Track, Queue, PartOfDayEnum
from radio.lib.decorators import authorize

from datetime import datetime
ERROR_TRACK_NAME = "Трек з такою назвою вже є в базі"


class TrackView(MethodView):

    @authorize
    def get(self, track_id: int):
        track = db.session.query(Track).filter(
            Track.id == track_id
        ).first()
        response = dict(
            id=track.id,
            name=track.name,
        ) if track else {}
        return jsonify(response)


class MusicView(MethodView):

    @authorize
    def get(self):
        tracks = db.session.query(Track).all()
        response = [dict(
            id=track.id,
            name=track.name,
        ) for track in tracks]

        return jsonify(response)

    @authorize
    def post(self):
        data = request.json
        name = data["name"]
        filepath = data["filepath"]
        duration = data["duration"]

        track = db.session.query(
            Track
        ).filter(
            name=name
        ).first()
        if track:
            return jsonify({"error": ERROR_TRACK_NAME}), 200

        track = Track(
            name=name,
            filepath=filepath,
            duration=duration
        )
        db.session.add(track)
        db.session.commit()
        response = dict(
            id=track.id,
            name=track.name,
        ) if track else dict(
            error="error?"
        )
        return jsonify(response), 200


class QueueView(MethodView):

    @authorize
    def get(self):
        data = request.json
        day = data["day"]
        part_of_day = data["part_of_day"]
        tracks = db.session.query(
            Queue
        ).filter(
            Queue.day == day,
            Queue.part == part_of_day
        ).all()
        response = [dict(
            id=track.track.id,
            name=track.track.name,
        ) for track in tracks]

        return jsonify(response)

    @authorize
    def post(self):
        data = request.json
        name = data["name"]
        filepath = data["filepath"]
        duration = data["duration"]
        day = datetime.strptime(data["day"], '%Y-%m-%d')
        track = Track(
            name=name,
            filepath=filepath,
            duration=duration
        )
        db.session.add(track)
        db.session.flush()

        part_of_day = data["part_of_day"]
        queue = Queue(
            track_id=track.id,
            part=part_of_day,
            day=day
        )
        db.session.add(queue)
        db.session.commit()

        response = dict(
            id=track.id,
            name=track.name,
        ) if track else dict(
            error="error?"
        )

        return jsonify(response), 200
