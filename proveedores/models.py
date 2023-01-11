from django.db import models

# Create your models here.
class Proveedores(models.Model):
    nombreEmpresa= models.CharField(max_lenght=100, verbose_name="Nombre Empresa")
    email= models.CharField(max_lenght=100, verbose_name="Correo electrónico")
    telefono= models.CharField(max_lenght=20, verbose_name="Teléfono")
    direccion= models.CharField(max_lenght=50, verbose_name="Dirección")   
    razonsocial= models.CharField(max_lenght=50, verbose_name="Razón social")
    rut= models.CharField(unique=True, max_lenght=10, verbose_name="Código RUT")
