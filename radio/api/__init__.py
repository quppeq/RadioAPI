from flask import Blueprint, Flask

def set_up_api(app: Flask):

    from .ping import Version

    mod = Blueprint('api', __name__)

    # Добавлення всіх правил для Блюпрінта
    mod.add_url_rule(
        '/version',
        view_func=Version.as_view('ApiVersion'),
    )

    # Реєстрація блюпрінта
    app.register_blueprint(mod, url_prefix='/api')
