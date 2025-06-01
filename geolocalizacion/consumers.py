from channels.generic.websocket import AsyncWebsocketConsumer
import json

class GeoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.mandado_id = self.scope['url_route']['kwargs']['mandado_id']
        self.rol = self.scope['url_route']['kwargs']['yo']  # 'cliente' o 'repartidor'
        self.group_name = f"ubicacion_mandado_{self.mandado_id}"

        # Unirse al grupo común
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        lat = data.get('lat')
        lng = data.get('lng')

        # Solo el repartidor puede enviar ubicación
        if self.rol == "repartidor":
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'send_location',
                    'lat': lat,
                    'lng': lng,
                    'rol': self.rol
                }
            )

    async def send_location(self, event):
        await self.send(text_data=json.dumps({
            'lat': event['lat'],
            'lng': event['lng'],
            'rol': event['rol']
        }))
