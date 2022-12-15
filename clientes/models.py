from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre= models.CharField(max_lenght=50, verbose_name="Nombre")
    apellido= models.CharField(max_lenght=50, verbose_name="Apellido")
    documento= models.CharField(unique=True, max_lenght=10, verbose_name="Documento")
    telefono= models.CharField(unique=True, max_lenght=10, verbose_name="Teléfono")