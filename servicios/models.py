from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from ciudad.models import Ciudad
from tecnico.models import Tecnico
from tipodeservicio.models import TipoServicio

#Create your models here.


class Servicio(models.Model):
    fecha= models.DateTimeField(verbose_name="Fecha", auto_now_add=True, editable=False, null=True)
    tipoServicio= models.ForeignKey(TipoServicio, on_delete=models.CASCADE, verbose_name="Tipo de Servicio", null=True)
    tecnico= models.ForeignKey(Tecnico, on_delete=models.CASCADE, verbose_name="Técnico", blank=True, null=True)
    ciudad= models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad", null=True)
    valorServicio = models.PositiveBigIntegerField(validators = [ MinValueValidator ( 0 )], null=True, verbose_name="Valor Servicio")
    class Iva(models.TextChoices):
        BYS='5', _('Bienes y Servicios')   
        EX='0', _('Exento')    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')   
    porcentajeIva=models.CharField(max_length=2, choices=Iva.choices, default=Iva.BYS, verbose_name="IVA")
    valorTotal= models.PositiveBigIntegerField(validators = [ MinValueValidator ( 0 )], blank=True, null=True, verbose_name="Valor Total")
    estado= models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado",null=True)
    observacion= models.CharField(max_length=300, verbose_name="Observación", null=True)

    def __str__(self)->str:
        return "%s %s" %(self.id, self.tipoServicio)  
    
    class Meta:
        ordering = ['tipoServicio']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'