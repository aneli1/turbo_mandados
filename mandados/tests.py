# Este archivo contiene pruebas para la funcionalidad de creación de mandados en la aplicación Mandados.
import pytest
from django.urls import reverse
from login_registro.models import Usuario
from mandados.models import Mandado 
import json
from django.contrib.auth.hashers import make_password 

@pytest.fixture
def usuario_existente(db):
    return Usuario.objects.create(
        nombre='Luis',
        apellidos='Lopez',
        correo='luis@example.com',
        password=make_password('secure123') #is for a test
    )

@pytest.fixture
def usuario_logueado(client, usuario_existente):
    # Simula el login del usuario
    session = client.session
    session['usuario_id'] = usuario_existente.id # asiminos que tu sesión guarda el ID del usuario
    session.save()
    return client

@pytest.mark.django_db
def test_crear_mandado_exitoso(usuario_logueado, usuario_existente):
    mandado_data = {
        'titulo': 'Entrega de paquete',
        'descripcion': 'Entregar paquete a la dirección indicada',
        'costo': '100.00', # Los campos de costo suelen ser DecimalField, mejor enviar como string
        'numContacto': '1234567890'
    }
    response = usuario_logueado.post(reverse('crear_mandado'), mandado_data)

    # La respuesta debe ser JSON y exitosa
    assert response.status_code == 200
    json_response = json.loads(response.content)
    assert json_response['success'] is True
    assert json_response['mensaje'] == 'Mandado creado exitosamente.'

    # Verificar que el mandado se haya creado en la base de datos
    mandado_creado = Mandado.objects.get(titulo='Entrega de paquete')
    assert mandado_creado.idUsuario == usuario_existente
    assert float(mandado_creado.costo) == 100.00 # Convertir a float si 
    assert mandado_creado.numContacto == '1234567890'


@pytest.mark.django_db
def test_crear_mandado_usuario_no_autenticado(client):
    mandado_data = {
        'titulo': 'Mandado sin login',
        'descripcion': 'Debe ser rechazado',
        'costo': '50.00',
        'numContacto': '0987654321'
    }
    # No se establece 'usuario_id' en la sesión del cliente
    response = client.post(reverse('crear_mandado'), mandado_data)

    assert response.status_code == 200 # JsonResponse devuelve 200 incluso para errores lógicos
    json_response = json.loads(response.content)
    assert json_response['success'] is False
    assert json_response['mensaje'] == 'Usuario no autenticado.'
    # mandado no creado en la db
    assert not Mandado.objects.filter(titulo='Mandado sin login').exists()


@pytest.mark.django_db
def test_crear_mandado_campos_faltantes(usuario_logueado):
    """
    Verifica que la creación de un mandado falla si faltan campos obligatorios.
    """
    mandado_data_incompleta = {
        'titulo': 'Incompleto',
        'descripcion': 'Falta el costo y contacto'
        # Faltan 'costo' y 'numContacto'
    }
    response = usuario_logueado.post(reverse('crear_mandado'), mandado_data_incompleta)

    assert response.status_code == 200
    json_response = json.loads(response.content)
    assert json_response['success'] is False
    assert json_response['mensaje'] == 'Todos los campos son obligatorios.'
    assert not Mandado.objects.filter(titulo='Incompleto').exists()

