from flask import Blueprint, Flask
from .radio import RadioView


def set_up_view(app: Flask):
    mod = Blueprint('', __name__)

    mod.add_url_rule(
        '',
        view_func=RadioView.as_view('RadioView'),
    )
    # Реєстрація блюпрінта
    app.register_blueprint(mod, url_prefix='/')
