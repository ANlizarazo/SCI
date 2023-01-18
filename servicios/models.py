from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from tecnico.models import Tecnico

# Create your models here.
class TipoServicio(models.Model):
    nombreServicio= models.CharField(max_length=50, verbose_name="Nombre de Servicio")
    descripcion= models.CharField(max_length=300, verbose_name="Descripción del Servicio")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')   
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

class Servicio(models.Model):
    observacion= models.CharField(max_length=200, verbose_name="Observaciones")
    fechaInicio= models.DateTimeField('%Y-%m-%d')
    fechaEntrega= models.DateTimeField('%Y-%m-%d')   
    precio= models.PositiveBigIntegerField(validators=[MinValueValidator(1)], verbose_name="Precio")
    observacionFinal= models.CharField(max_length=250, verbose_name="Orservación Final")
    tipoServicio= models.ForeignKey(TipoServicio, on_delete=models.CASCADE, verbose_name="Tipo de Servicio",null=True)
    tecnico= models.ForeignKey(Tecnico, on_delete=models.CASCADE, verbose_name="Técnico",null=True)
