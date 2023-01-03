from django.db import models

# Create your models here.

class Compras(models.Model):
    referencias= models.CharField(max_lenght=50, verbose_name="Referencias")
    proveedor= models.CharField(max_lenght=50, verbose_name="Proovedor")
    fecha= models.CharField(max_lenght=50, verbose_name="Fecha")