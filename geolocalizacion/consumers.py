from channels.generic.websocket import AsyncWebsocketConsumer
import json

class GeoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.mandado_id = self.scope['url_route']['kwargs']['mandado_id']
        self.cliente_id = self.scope['url_route']['kwargs']['cliente_id']
        self.repartidor_id = self.scope['url_route']['kwargs']['repartidor_id']
        self.rol = self.scope['url_route']['kwargs']['yo']  # 'cliente' o 'repartidor'
        self.group_name = f"ubicacion_mandado_{self.mandado_id}"

        # Unirse al grupo
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Salir del grupo
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
#        # Cerrar la conexión
        # await self.close()  # No es necesario, el canal se cierra automáticamente 
    async def receive(self, text_data):# Recibir datos del WebSocket
        data = json.loads(text_data)
        lat = data.get('lat')
        lng = data.get('lng')

        if lat is None or lng is None:
            # Ignorar si no hay datos válidos
            return

        # Enviar al grupo la ubicación junto con el rol del que envía
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
        # No enviar la ubicación al mismo usuario que la envió (evitar eco)
        if event['rol'] == self.rol:
            return

        await self.send(text_data=json.dumps({
            'lat': event['lat'],
            'lng': event['lng'],
            'rol': event['rol']
        }))
