from django.db import models
from django.utils.translation import gettext_lazy as _



# Create your models here.

class Ciudad(models.Model):
    nombre= models.CharField(max_length=60, unique=True, verbose_name="Ciudad")
    
    def __str__(self)->str:
        return "%s" %(self.nombre)  
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        
class Cliente(models.Model):
    nombreEmpresa= models.CharField(max_length=100, verbose_name="Nombre Empresa")
    nit= models.CharField(unique=True, max_length=20, verbose_name="NIT")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    email=models.CharField(max_length=100, verbose_name="Correo Electrónico")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad", blank=True, null=True)
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    
    def __str__(self)->str:
        return "%s" %(self.nombreEmpresa)  

    class Meta:
        ordering = ['nombreEmpresa']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    