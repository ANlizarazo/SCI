from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_lenght=50, verbose_name="Nombre") 
    precio = models.BigIntegerField(validadores = [ MinValueValidator ( 0 )], verbose_name="Precio")   
    especificaciones = models.CharField(max_lenght=200, verbose_name="Especificaciones")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    stock = models.BigIntegerField(validadores = [ MinValueValidator ( 0 )], verbose_name="Cantidad") 
    porcentajeIva= models.BigInt(max_length=10, verbose_name="Porcentaje IVA")
    categoria = models.CharField(max_lenght=50, verbose_name="Categoría")