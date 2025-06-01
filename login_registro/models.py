from django.db import models

# Modelo que representa a un usuario en el sistema
class Usuario(models.Model):
    # Campo para el nombre del usuario
    nombre = models.CharField(max_length=15)

    # Campo para el apellido del usuario
    apellidos = models.CharField(max_length=100)

    # Campo para el correo electrónico, debe ser único
    correo = models.EmailField(unique=True)

    # Campo para almacenar la contraseña (debe estar hasheada en la lógica del sistema)
    password = models.CharField(max_length=255)

    # Representación legible del objeto cuando se imprime o se consulta desde el admin
    def __str__(self):
        return self.nombre