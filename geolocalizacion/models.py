from django.db import models

class Location(models.Model):
    user_id = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ubicación de usuario {self.user_id} - {self.lat}, {self.lng}"
