from django.db import models
from django.utils import timezone


# Create your models here.

class Automovil(models.Model):
    Marca = models.TextField()
    Modelo = models.TextField()
    Anio = models.TextField()
    Color = models.TextField()
    NroPuertas = models.TextField()
    Descripcion = models.TextField()
    Precio = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()