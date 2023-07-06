from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from ciudad.models import Ciudad
from tecnico.models import Tecnico
from tipodeservicio.models import TipoServicio

#Create your models here.


class Servicio(models.Model):
    fecha= models.DateTimeField(verbose_name="Fecha", auto_now_add=True, editable=False, )
    observacion= models.TextField(max_length=300,blank= True,null= True, verbose_name="Observación")
    observacionFinal= models.TextField(max_length=300,blank= True,null= True, verbose_name="Observación Final")
    class Iva(models.TextChoices):
        BYS='5', _('Bienes y Servicios')
        GR='19', _('General')    
        EX='0', _('Exento')
    porcentajeIva=models.DecimalField(validators=[MinValueValidator(0.0)], decimal_places=1, max_digits=20,max_length=3, choices=Iva.choices, default=Iva.GR, verbose_name="IVA")
    valorTotal= models.PositiveBigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')   
    estado= models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    tipoServicio= models.ForeignKey(TipoServicio, on_delete=models.CASCADE, verbose_name="Tipo de Servicio",null=True)
    ciudad= models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad")
    tecnico= models.ForeignKey(Tecnico, on_delete=models.CASCADE, verbose_name="Técnico", blank=True, null=True)
    
    def __str__(self)->str:
        return "%s %s" %(self.id, self.tipoServicio)  
    
    class Meta:
        ordering = ['tipoServicio']
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'