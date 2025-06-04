from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(
        r'^ws/ubicacion/(?P<mandado_id>\d+)/(?P<cliente_id>\d+)/(?P<repartidor_id>\d+)/(?P<yo>(cliente|repartidor))/$',
        consumers.GeoConsumer.as_asgi()
    ),
]