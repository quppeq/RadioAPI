from db import db
from enum import Enum
from sqlalchemy.orm import relationship


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
    )
    filepath = db.Column(
        db.String(255)
    )
    duration = db.Column(
        db.Integer,
        nullable=True
    )


class PartOfDayEnum(Enum):
    morning = 1
    afternoon = 2
    evening = 3


class Queue(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'))
    day = db.Column(db.Date, nullable=False)
    part = db.Column(db.Integer, nullable=False)

    track = relationship('Track')
