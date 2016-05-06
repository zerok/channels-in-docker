from channels.routing import route

from . import consumers


channel_routing = [
    route("websocket.connect", consumers.ws_connect),
    route("websocket.disconnect", consumers.ws_disconnect),
    route('websocket.receive', consumers.ws_receive),
]
