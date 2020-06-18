from flask import Blueprint, Flask
from .radio import RadioView, RadioHistoryView
from .login import LoginView, LogoutView
from radio.lib.login import g_login


def set_up_view(app: Flask):
    mod = Blueprint('', __name__)

    mod.add_url_rule(
        '',
        view_func=RadioView.as_view('RadioView'),
    )

    mod.add_url_rule(
        'history',
        view_func=RadioHistoryView.as_view('RadioHistoryView'),
    )

    mod.add_url_rule(
        'login',
        view_func=LoginView.as_view('LoginView'),
    )

    mod.add_url_rule(
        'logout',
        view_func=LogoutView.as_view('LogoutView'),
    )

    mod.before_request(g_login)

    # Реєстрація блюпрінта
    app.register_blueprint(mod, url_prefix='/')
