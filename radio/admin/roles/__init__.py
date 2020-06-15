from flask import g
from flask.views import MethodView
from radio.models.user import Role


class RoleView(MethodView):

    def get(self):
        """Отримати роль"""
        raise NotImplementedError

    def post(self):
        """Створити роль"""
        raise NotImplementedError

    def delete(self):
        """Видалити роль"""
        raise NotImplementedError


class RoleUserView(MethodView):

    def get(self):
        """Отримати ролі користувача (можливо юзлес)"""
        raise NotImplementedError

    def post(self):
        """добавити роль користувачу"""
        raise NotImplementedError

    def delete(self):
        """видалити роль користувача"""
        raise NotImplementedError
