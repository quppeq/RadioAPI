from flask import g, abort
from radio.lib.decorators import authorize
ADMIN_ROLE = 'admin'


@authorize
def is_admin_view():
    if not any(role.name == ADMIN_ROLE for role in g.user.roles):
        abort(403)