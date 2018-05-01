from channels.consumer import SyncConsumer, AsyncConsumer


class ApplicationConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connect received")
        await self.channel_layer.group_add('custom_broadcast', self.channel_name)
        await self.send({
            'type': 'websocket.accept',
        })

    async def websocket_disconnect(self, event):
        print("Disconnect received")
        await self.channel_layer.group_discard('custom_broadcast', self.channel_name)

    async def websocket_receive(self, event):
        print("Data received")
        await self.channel_layer.group_send('custom_broadcast', {
            'type': 'chat.message',
            'text': event['text'],
        })

    async def chat_message(self, event):
        await self.send({
            'type': 'websocket.send',
            'text': event['text'],
        })