from django.http import HttpResponse
from channels.handler import AsgiHandler


def http_request(message):
    response = HttpResponse("Hello world from a consumer!")
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
