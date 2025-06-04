from django.db import models
from login_registro.models import Usuario  

class Location(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='locations')
    lat = models.FloatField()
    lng = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['user', 'timestamp']),
        ]

    def __str__(self):
        return f"Ubicación de usuario {self.user.id} - {self.lat}, {self.lng}"
