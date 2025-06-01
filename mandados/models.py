from django.db import models
from login_registro.models import Usuario
from django.utils import timezone

class Mandado(models.Model):
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mandados_publicados')
    repartidor = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL, related_name='mandados_aceptados')
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    numContacto = models.CharField(max_length=20)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.titulo} - {self.idUsuario.nombre}"
