from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Create your models here.

class Servicio(models.Model):
    observacion= models.CharField(max_length=200, verbose_name="Observaciones")
    fechaInicio= models.DateTimeField('%Y-%m-%d %H:%M:%S', verbose_name="Fecha de Inicio")
    fechaEntrega= models.DateTimeField('%Y-%m-%d %H:%M:%S', verbose_name="Fecha de Entrega")   
    precio= models.PositiveBigIntegerField(validators=[MinValueValidator(1)], verbose_name="Precio")
    observacionFinal= models.CharField(max_length=250, verbose_name="Orservación Final")
    tipodeservicio=models.CharField(max_length=50, verbose_name="Tipo de servicio")
    tecnico=models.CharField(max_length=50, verbose_name="Técnico")