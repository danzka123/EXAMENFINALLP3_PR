from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=10)
    precio_compra = models.CharField(max_length=10)
    precio_venta = models.CharField(max_length=10)
    fecha_compra = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    estado = models.CharField(max_length=1)
    