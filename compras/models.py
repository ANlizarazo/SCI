from django.db import models
from django.core.validators import MinValueValidator
from django.utils.formats import get_format
from proveedores.models import Proveedor
# Create your models here.


class Compra(models.Model):
    fecha= models.DateTimeField('%Y-%m-%d %H:%M:%S')

class DetalleCompra(models.Model):
    cantidadMaterial = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Cantidad Material") 
    valorTotalMaterial = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total Material")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor")