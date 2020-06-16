from flask import current_app
import json
import telnetlib
from .models import Track


ON_AIR = b"json.on_air"
PUSH_TRACK = b"request.push file://%s"

EOF = b"END"
END = b"\nexit\n"


def get_now() -> Track:
    host = current_app.config.get("RADIO_URL", "127.0.0.1")
    port = current_app.config.get("RADIO_PORT", "1234")
    with telnetlib.Telnet(host, port) as t:
        t.write(ON_AIR + b"\n")
        mess = t.read_until(EOF)
        mess = mess[:-5]
        mess = json.loads(mess)
        t.write(END)
    return Track.from_dict(mess)


def put_in_queue(track_path: str):
    host = current_app.config.get("RADIO_URL", "127.0.0.1")
    port = current_app.config.get("RADIO_PORT", "1234")
    with telnetlib.Telnet(host, port) as t:
        t.write(PUSH_TRACK % track_path.encode())
        t.write(END)
    return {}
