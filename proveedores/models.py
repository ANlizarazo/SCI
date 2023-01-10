from django.db import models

# Create your models here.
class Proveedor(models.Model):
    razonSocial= models.CharField(max_length=50, verbose_name="Razón social")
    nombreEmpresa= models.CharField(max_length=50, verbose_name="Nombre de la empresa")
    rut= models.CharField(unique=True, max_length=10, verbose_name="Codigo RUT")
    direccion= models.CharField(max_length=50, verbose_name="Dirección")
    ciudad= models.CharField(max_length=50, verbose_name="Ciudad")
    email= models.CharField(unique=True, max_length=10, verbose_name="Correo electrónico")
    telefono= models.CharField(unique=True, max_length=10, verbose_name="Teléfono")
