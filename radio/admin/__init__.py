from flask import Blueprint, Flask


def set_up_admin(app: Flask):
    from .roles.helpers import is_admin_view
    mod = Blueprint('admin', __name__)

    # Дивимось на ролі
    app.before_request(is_admin_view)

    # Реєстрація блюпрінта
    app.register_blueprint(mod, url_prefix='/admin')
