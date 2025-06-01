from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/ubicacion/(?P<mandado_id>\d+)/(?P<yo>\w+)/$', consumers.GeoConsumer.as_asgi()),
]
