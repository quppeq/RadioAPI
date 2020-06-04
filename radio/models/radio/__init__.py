from db import db


class Track(db.Model):

    id = db.Column(db.Integer, primary_key=True)
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