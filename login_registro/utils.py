#pruebas unitarias
from django.contrib.auth.hashers import check_password
from .models import Usuario

def verificar_usuario(correo, password):
    try:
        usuario= Usuario.objects.get(correo=correo)
        return check_password(password, usuario.password)
    except Usuario.DoesNotExist:
        return False

def correo_ya_registrado(correo):
    return Usuario.objects.filter(correo=correo).exists()


