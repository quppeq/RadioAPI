from flask import Blueprint, Flask

def set_up_api(app: Flask):

    from .ping import VersionView
    from .music import TrackView, MusicListView

    mod = Blueprint('api', __name__)

    # Добавлення всіх правил для Блюпрінта
    mod.add_url_rule(
        '/version',
        view_func=VersionView.as_view('ApiVersion'),
    )

    mod.add_url_rule(
        '/music/list',
        view_func=MusicListView.as_view('ApiMusicList'),
    )

    mod.add_url_rule(
        '/music/<int:track_id>',
        view_func=TrackView.as_view('ApiTrack'),
    )

    # Реєстрація блюпрінта
    app.register_blueprint(mod, url_prefix='/api')
