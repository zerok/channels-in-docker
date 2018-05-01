from channels.routing import ProtocolTypeRouter
from . import consumers


application = ProtocolTypeRouter({
    'websocket': consumers.ApplicationConsumer,
})