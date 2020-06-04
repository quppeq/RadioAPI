from flask import Blueprint, Flask

def set_up_api(app: Flask):

    from .ping import Ping

    mod = Blueprint('api', __name__)
    mod.add_url_rule(
        '/ping',
        view_func=Ping.as_view('ApiPing'),
    )
    app.register_blueprint(mod, url_prefix='/api')
