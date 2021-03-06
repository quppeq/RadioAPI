import os
from flask import Flask
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
import logging
import subprocess

from db import db
from .api import set_up_api
from .admin import set_up_admin
from .view import set_up_view
from .config import Config


log = logging.getLogger(__name__)
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'static')
TEMPLATE_FOLDER = os.path.join(ROOT_FOLDER, 'templates')


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
    set_up_admin(app)
    set_up_view(app)


class RadioApp(Flask):

    def __init__(self, *args, **kw):
        static_folder = None if os.getenv('STATIC_URL') else STATIC_FOLDER
        template_folder = None if os.getenv('TEMPLATE_URL') else TEMPLATE_FOLDER
        super().__init__(*args, static_folder=static_folder, template_folder=template_folder, **kw)
        self.version = os.getenv('VERSION')
        self.logger_name = 'RadioApp'

    @property
    def logger(self):
        return logging.getLogger(self.logger_name)


def create_app():
    app = RadioApp(__name__)
    version = subprocess.check_output(["git", "describe", "--always", "--dirty", "--tags"]).strip()
    version = version.decode()
    app.config.from_object(Config)
    app.config["VERSION"] = version

    configure_db(app)
    configure_migration(app, db)
    configure_blueprints(app)

    app.manager = configure_manager(app)
    return app
