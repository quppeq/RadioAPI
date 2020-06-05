from db import db
import datetime


UserRole = db.Table(
    'user_role', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)


class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)


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

    last_auth = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    roles = db.relationship('Role', secondary=UserRole)

