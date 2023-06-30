from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from tipodeservicio.models import TipoServicio

#Create your models here.


class Servicio(models.Model):
    observacion= models.CharField(max_length=200, verbose_name="Observación")
    observacionFinal= models.CharField(max_length=250, verbose_name="Observación Final")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')   
    tipoServicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE, verbose_name="Tipo de Servicio",null=True, blank=True)
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    
    def __str__(self)->str:
        return "%s %s" %(self.id, self.tipoServicio)  
    
    class Meta:
        ordering = ['tipoServicio']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'