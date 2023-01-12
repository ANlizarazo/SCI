from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre Producto") 
    precio = models.BigIntegerField(validators = [ MinValueValidator ( 1 )], verbose_name="Precio")   
    especificaciones = models.CharField(max_length=300, verbose_name="Especificaciones")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    stock = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Cantidad") 
    porcentajeIva= models.BigIntegerField(max_length=10, verbose_name="Porcentaje IVA")
    categoria = models.CharField(max_length=50, verbose_name="Categoría")

