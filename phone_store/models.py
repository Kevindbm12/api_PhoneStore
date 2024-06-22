from django.db import models

# Crear tus modelos aquí.
class Marca(models.Model):
    nombre = models.CharField(max_length=255)


class Celular(models.Model):
    modelos = models.CharField(max_length=255)
    descripción = models.TextField(blank=True)
    precio = models.FloatField()
    fecha_lanzamiento = models.DateField()
    image_url = models.URLField(max_length=255, blank=True, null=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)


class Especificaciones(models.Model):
    nombre = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    celular = models.ForeignKey(Celular, on_delete=models.CASCADE)
