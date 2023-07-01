from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from ciudad.models import Ciudad
from tecnico.models import Tecnico
from tipodeservicio.models import TipoServicio

#Create your models here.


class Servicio(models.Model):
    fecha= models.DateTimeField(verbose_name="Fecha", auto_now_add=True, editable=False, null=True)
    observacion= models.CharField(max_length=200, verbose_name="Observación", null=True)
    observacionFinal= models.CharField(max_length=250, verbose_name="Observación Final", null=True)
    porcentajeIva=models.DecimalField(validators=[MinValueValidator(0.0)], decimal_places=1, max_digits=20, verbose_name="Porcentaje IVA", null=True)
    valorTotal= models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total", null=True)
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')   
    tipoServicio= models.ForeignKey(TipoServicio, on_delete=models.CASCADE, verbose_name="Tipo de Servicio",null=True)
    estado= models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    ciudad= models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad",null=True)
    tecnico= models.ForeignKey(Tecnico, on_delete=models.CASCADE, verbose_name="Técnico",null=True, blank=True)
    
    def __str__(self)->str:
        return "%s %s" %(self.id, self.tipoServicio)  
    
    class Meta:
        ordering = ['tipoServicio']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'