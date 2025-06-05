import pytest
from django.urls import reverse
from django.test import Client

@pytest.mark.django_db
def test_enviar_ubicacion_view():
    client = Client()
    url = reverse('enviar_ubicacion', args=[123])
    response = client.get(url)
    assert response.status_code == 200
    assert b"123" in response.content

@pytest.mark.django_db
def test_seguimiento_view():
    client = Client()
    url = reverse('seguimiento', args=[1, 100, 200, 'cliente'])
    response = client.get(url)
    assert response.status_code == 200
    assert b"1" in response.content
    assert b"100" in response.content
    assert b"200" in response.content
    assert b"cliente" in response.content
