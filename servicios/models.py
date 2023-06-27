from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from tecnico.models import Tecnico

#Create your models here.
class TipoServicio(models.Model):
    nombreServicio= models.CharField(max_length=50, verbose_name="Nombre de Servicio")
    descripcion= models.CharField(max_length=300, verbose_name="Descripción del Servicio")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')   
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self)->str:
        return "%s" %(self.nombreServicio)  
    
    class Meta:
        ordering = ['nombreServicio']
        verbose_name = 'Tipo de Servicio'
        verbose_name_plural = 'Tipos de Servicios'

class Servicio(models.Model):
    observacion= models.CharField(max_length=200, verbose_name="Observaciones")
    fechaInicio= models.DateTimeField(verbose_name="Fecha de Inicio",help_text= "DD/MM/AAA")
    fechaEntrega= models.DateTimeField(verbose_name="Fecha de Entrega",help_text= "DD/MM/AAAA")
    precio= models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name="Precio")
    observacionFinal= models.CharField(max_length=250, verbose_name="Observación Final")
    class TipoServicio(models.TextChoices):
        MON='Montaje', _('Montaje')
        DES='Desmontaje', _('Desmontaje')
        TRA='Transporte', _('Transporte')
        OT='Otro', _('Otro') 
    tipoServicio=models.CharField(max_length=12, choices=TipoServicio.choices, verbose_name="Tipo de Servicio", null = True)    
    tecnico= models.ForeignKey(Tecnico, on_delete=models.CASCADE, verbose_name="Técnico", null=True, blank=True)
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
    estado=models.CharField(max_length=10, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado", blank=True, null=True)

    def __str__(self)->str:
        return "%s %s" %(self.id, self.tipoServicio)  
    
    class Meta:
        ordering = ['fechaInicio']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'