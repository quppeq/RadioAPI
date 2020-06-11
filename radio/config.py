from os import environ


class Config:
    BOT_SHARED_SECRET = environ["RADIOAPI_BOT_SECRET"]
    SQLALCHEMY_DATABASE_URI = environ.get("RADIOAPI_DB_URI", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
