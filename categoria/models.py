from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Create your models here.

class Categoria(models.Model):
    nombrecat = models.CharField(max_length=60, verbose_name="Nombre Categoría", null=True, blank=True) 
    descripcioncat = models.TextField(max_length=300, verbose_name="Descripción")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estadocat=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado", null=True, blank=True)

    def __str__(self)->str:
        return "%s" %(self.nombrecat)  
    
    class Meta:
        ordering = ['nombrecat']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
