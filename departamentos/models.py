from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Departamento(models.Model):
    nombre=models.CharField(max_length=90,unique=True, verbose_name="Nombre Departamento")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self)->str:
        return "%s" %(self.nombre)
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


