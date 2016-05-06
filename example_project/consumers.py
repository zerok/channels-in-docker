from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group


def http_request(message):
    response = HttpResponse("Hello world from a consumer!")
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)


def ws_connect(msg):
    Group('custom_broadcast').add(msg.reply_channel)


def ws_disconnect(msg):
    Group('custom_broadcast').discard(msg.reply_channel)


def ws_receive(msg):
    Group('custom_broadcast').send({
        'text': msg.content['text']
    })
