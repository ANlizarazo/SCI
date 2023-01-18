from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


# Create your models here.

class Tecnico(models.Model):
    nombres=models.CharField(max_length=50, verbose_name="Nombres")
    apellidos=models.CharField(max_length=50, verbose_name="Apellidos")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    class Genero(models.TextChoices):
        FE='F', _('Femenino')
        MA='M', _('Masculino')
        OT='O', _('Otro')    
    class TipoDocumento(models.TextChoices):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')
        OT='OT', _('Otro') 
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    genero=models.CharField(max_length=3, choices=Genero.choices, verbose_name="Género") 
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, verbose_name="Tipo de Documento")
    numDocumento=models.CharField(max_length=20, verbose_name="Número de Documento")

