from django.db import models
from django.core.validators import MinValueValidator
from django.utils.formats import get_format
from proveedores.models import Proveedor
from usuarios.models import Usuario
# Create your models here.

class DetalleCompra(models.Model):
    cantidadMaterial = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Cantidad Material") 
    valorTotalMaterial = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total Material")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor")

class Compra(models.Model):
    fecha= models.DateTimeField('%Y-%m-%d %H:%M:%S')
    detalleCompra = models.ForeignKey(DetalleCompra, on_delete=models.CASCADE, verbose_name="Detalle Compra")
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")