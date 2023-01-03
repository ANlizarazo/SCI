from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_lenght=60, verbose_name="Nombre")    
    categorias = models.CharField(max_lenght=50, verbose_name="Categoría")
    descripcion = models.CharField(max_lenght=100, verbose_name="Descripción")
    precio = models.CharField(max_lenght=50, verbose_name="Precio")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")