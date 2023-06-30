from django.db import models
from django.utils.translation import gettext_lazy as _
from departamentos.models import Departamento

# Create your models here.
class Ciudad(models.Model):
    nombre= models.CharField(max_length=60, unique=True, verbose_name="Ciudad")
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="Departamento")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    
    def __str__(self)->str:
        return "%s" %(self.nombre)  
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'