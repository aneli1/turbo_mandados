#Este archivo contiene las pruebas unitarias para las funciones de verificación de usuario y correo electrónico.
import pytest
from login_registro.models import Usuario
from login_registro.utils import verificar_usuario, correo_ya_registrado
from django.contrib.auth.hashers import make_password

@pytest.mark.django_db
def test_verificar_usuario_valido():
    usuario= Usuario.objects.create(
        nombre="Ane",
        apellidos="Jiménez",
        correo="ane@gmail.com",
        password=make_password("aaa...aaa") 
    )
    assert verificar_usuario("ane@gmail.com", "aaa...aaa") is True

@pytest.mark.django_db
def test_verificar_credenciales_incorrectas():
    usuario = Usuario.objects.create(
        nombre="Ane",
        apellidos="Jiménez",
        correo="ane@gmail.com",
        password=make_password("aaa...aaa")
    )
    assert verificar_usuario("ane@gmail.com", "patitoJuan") is False

@pytest.mark.django_db
def test_correo_ya_registrado():
    usuario = Usuario.objects.create(
        nombre="Ane",
        apellidos="Jiménez",
        correo="a@gmail.com",
        password=make_password("aaa...aaa")
    )
    assert correo_ya_registrado("a@gmail.com") is True
    assert correo_ya_registrado("ajam@gmail.com") is False

@pytest.mark.django_db
def test_verificar_usuario_no_existe():
    assert verificar_usuario("noexiste@gmail.com","aajajaj") is False
                                