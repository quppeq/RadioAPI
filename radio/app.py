import os
from flask import Flask
import logging

log = logging.getLogger(__name__)
ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'static')


class RadioApp(Flask):

    def __init__(self, *args, **kw):
        static_folder = None if os.getenv('STATIC_URL') else STATIC_FOLDER
        super().__init__(*args, static_folder=static_folder, **kw)
        self.version = os.getenv('VERSION')

    def logger(self):
        print("a")
        log.info("asd")
        print(self.logger_name)
        return logging.getLogger(self.logger_name)


def create_app():
    app = RadioApp(__name__)
    return app
