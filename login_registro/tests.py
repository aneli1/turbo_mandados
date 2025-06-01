import pytest
from django.urls import reverse
from login_registro.models import Usuario
from django.contrib.auth.hashers import make_password

@pytest.mark.django_db
def test_menu_principal(client):
    response = client.get(reverse('dashboard_view'))
    assert response.status_code == 200
    assert b'Turbo Mandados' in response.content

@pytest.mark.django_db
def test_registro_usuario_crea_usuario(client):
    dummy_password = "examplePass123!"
    data = {
        'nombre': 'Juan',
        'apellidos': 'Perez',
        'correo': 'juan@example.com',
        'password': dummy_password
    }
    response = client.post(reverse('registro_usuario'), data)
    assert Usuario.objects.filter(correo='juan@example.com').exists()
    assert response.status_code == 302

@pytest.mark.django_db
def test_login_usuario_valido(client):
    usuario = Usuario.objects.create(
        nombre='Luis',
        apellidos='Lopez',
        correo='luis@example.com',
        password=make_password('secure123')
    )
    dummy_pass = 'secure123'  # NOSONAR
    data = {'correo': 'luis@example.com', 'password': dummy_pass}
    response = client.post(reverse('login_usuario'), data)
    assert response.status_code == 302
    assert response.url == reverse('dashboard_view')

@pytest.mark.django_db
def test_login_usuario_invalido(client):
    data = {'correo': 'nobody@example.com', 'password': 'wrongpass'}
    response = client.post(reverse('login_usuario'), data)
    assert response.status_code == 200
    assert "Inicia sesión en tu cuenta" in response.content.decode("utf-8")
