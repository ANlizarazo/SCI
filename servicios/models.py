from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


#Create your models here.
class Servicio(models.Model):
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
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

