from channels.routing import route

from . import consumers


channel_routing = [
    route('http.request', consumers.http_request),
]
