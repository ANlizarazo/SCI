from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from servicios.models import Servicio 
from ventas.models import Venta

# Create your models here.

class Usuario(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="Nombres")
    apellidos=models.CharField(max_length=45, verbose_name="Apellidos")
    telefono=models.BigIntegerField(validators=[MinValueValidator(1)], verbose_name="Teléfono")
    email=models.CharField(max_length=100, verbose_name="Correo Electrónico")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    class TipoDocumento(models.Model):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')
        OT='OT', _('Otro') 
    class Genero(models.Model):
        FE='F', _('Femenino')
        MA='M', _('Masculino')
        OT='O', _('Otro')
    class Rol(models.Model):
        AD='Admin', _('Administrador')
        EM='Empl', _('Empleado')
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, verbose_name="Tipo de Documento")
    genero=models.CharField(max_length=3, choices=Genero.choices, verbose_name="Género")
    rol=models.CharField(max_length=2, choices=Rol.AD, verbose_name="Rol")
    numDocumento=models.PositiveBigIntegerField(validators=[MinValueValidator(1)], verbose_name="Número de Documento")
    servicio= models.ForeignKey(Servicio, on_delete=models.CASCADE, verbose_name="Servicio")
    venta= models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name="Venta")

    
