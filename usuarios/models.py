from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Create your models here.

class Usuario(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="Nombres")
    apellidos=models.CharField(max_length=45, verbose_name="Apellidos")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    class TipoDocumento(models.Model):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')    
    class Genero(models.Model):
        FE='F', _('Femenino')
        MA='M', _('Masculino')
        OT='O', _('Otro')
    class Rol(models.Model):
        AD='Admin', _('Administrador')
        EM='Empl', _('Empleado')
    class Estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    rol=models.CharField(max_length=2, choices=Rol.AD, verbose_name="Rol")
    tipoDocumento=models.CharField(max_length=3, choices=TipoDocumento.CC, verbose_name="Tipo de Documento")
    genero=models.CharField(max_length=3, choices=Genero.FE, verbose_name="Género")
    numDocumento=models.CharField(max_length=50, verbose_name="Número de Documento")
    email=models.CharField(max_length=100, verbose_name="Correo Electrónico")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    
