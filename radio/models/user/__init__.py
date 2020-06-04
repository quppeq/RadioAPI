from db import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    telegram_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
    )
    session_token = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
    )
