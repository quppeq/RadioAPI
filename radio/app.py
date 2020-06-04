import os
from flask import Flask
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
import logging
import subprocess

from db import db
from .api import set_up_api


log = logging.getLogger(__name__)
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'static')


def configure_db(app):
    db.init_app(app)

def configure_migration(app, db):
    return Migrate(app, db)

def configure_manager(app):
    manager = Manager(app)
    manager.add_command("runserver", Server(host='0.0.0.0', threaded=True))
    manager.add_command("db", MigrateCommand)
    return manager


def configure_blueprints(app):
    set_up_api(app)

class RadioApp(Flask):

    def __init__(self, *args, **kw):
        static_folder = None if os.getenv('STATIC_URL') else STATIC_FOLDER
        super().__init__(*args, static_folder=static_folder, **kw)
        self.version = os.getenv('VERSION')

    def logger(self):
        return logging.getLogger(self.logger_name)


def create_app():
    app = RadioApp(__name__)
    version = subprocess.check_output(["git", "describe", "--always", "--dirty", "--tags"]).strip()
    version = version.decode()
    app.config['VERSION'] = app.config.get('VERSION', version)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite://{ROOT_FOLDER}/db/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    configure_db(app)
    configure_migration(app, db)
    configure_blueprints(app)

    app.manager = configure_manager(app)
    return app
