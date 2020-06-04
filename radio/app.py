import os
from flask import Flask
import logging
import subprocess

from .api import set_up_api


log = logging.getLogger(__name__)
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'static')


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

    configure_blueprints(app)
    return app
