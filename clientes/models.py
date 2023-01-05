from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre= models.CharField(max_lenght=50, verbose_name="Nombre")
    apellido= models.CharField(max_lenght=50, verbose_name="Apellido")
    rut= models.CharField(unique=True, max_lenght=10, verbose_name="Codigo RUT")
    class TipoDocumento(models.Model):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')    
    tipoDocumento=models.CharField(max_length=3, choices=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numDocumento= models.CharField(unique=True, max_lenght=10, verbose_name="Número de Documento")
    telefono= models.CharField(unique=True, max_lenght=10, verbose_name="Teléfono")
    direccion=models.CharField(max_length=45, verbose_name="Dirección")
    email=models.CharField(max_length=100, verbose_name="Correo Electrónico")
    