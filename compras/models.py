from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Compras(models.Model):
    id= models.AutoField(unique= True, primary_key=True, verbose_name="ID Compra")
    fecha= models.DateField(max_length=25, verbose_name="Fecha")

class DetalleCompra(models.Model):
    id= models.AutoField(unique= True, primary_key=True, verbose_name="Número Factura")
    cantidadMaterial = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Cantidad Material") 
    valorTotalMaterial = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total Material")
    proveedor = models.CharField(max_length=100, verbose_name="Proveedor")
           