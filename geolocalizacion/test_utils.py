import pytest
from geolocalizacion.models import Location
from login_registro.models import Usuario

@pytest.mark.django_db
def test_creacion_location_valida():
    usuario = Usuario.objects.create(
        nombre="Prueba", apellidos="Test", correo="test@example.com", password="123"
    )

    ubicacion = Location.objects.create(
        user=usuario,
        lat=17.05,
        lng=-96.72
    )

    assert ubicacion.id is not None
    assert ubicacion.lat == 17.05
    assert ubicacion.lng == -96.72
    assert ubicacion.user == usuario