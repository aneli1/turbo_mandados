from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geopy.distance import geodesic
from .models import Location

# Vista para almacenar geolocalización vía API (si decides usarlo en un futuro)
class geolocalizacion_view(APIView):
    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vista tradicional para enviar ubicación (ya no se usa si solo repartidor transmite)
def enviar_ubicacion_view(request, repartidor_id):
    return render(request, 'geolocalizacion/enviar_ubicacion.html', {'repartidor_id': repartidor_id})

def seguimiento_view(request, mandado_id, cliente_id, repartidor_id, yo):
    context = {
        'mandado_id': mandado_id,
        'cliente_id': cliente_id,
        'repartidor_id': repartidor_id,
        'yo': yo,
    }
    return render(request, 'geolocalizacion/seguimiento.html', context)
