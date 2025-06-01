from django.urls import path
from . import views

urlpatterns = [
    path('enviar_ubicacion/<int:repartidor_id>/', views.enviar_ubicacion_view, name='enviar_ubicacion'),
    path('seguimiento/<int:mandado_id>/<str:yo>/', views.seguimiento_view, name='seguimiento'),
]