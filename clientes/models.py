from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre= models.CharField(max_lenght=50, verbose_name="Nombre")
    apellido= models.CharField(max_lenght=50, verbose_name="Apellido")
    telefono= models.CharField(max_lenght=50, verbose_name="Teléfono")