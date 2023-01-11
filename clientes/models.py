from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre= models.CharField(max_lenght=50, verbose_name="Nombre")
    apellido= models.CharField(max_lenght=50, verbose_name="Apellido")
    rut= models.CharField(unique=True, max_lenght=20, verbose_name="RUT")    
    numDocumento= models.CharField(unique=True, max_lenght=20, verbose_name="Número de Documento")
    telefono= models.CharField(max_lenght=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=50, verbose_name="Dirección")
    email=models.EmailField(max_length=100, verbose_name="Correo Electrónico")
    class TipoDocumento(models.Model):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')    
    class Estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    tipoDocumento=models.CharField(max_length=3, choices=TipoDocumento.CC, verbose_name="Tipo de Documento")
