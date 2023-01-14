from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from productos.models import Producto

# Create your models here.
class Ciudad(models.Model):
    nombre= models.CharField(max_length=60, verbose_name="Ciudad")
class Compra(models.Model):
    fecha= models.DateTimeField('%Y-%m-%d %H:%M:%S')
class Cliente(models.Model):
    nombre= models.CharField(max_length=100, verbose_name="Nombre")
    nit= models.CharField(unique=True, max_length=20, verbose_name="NIT")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    email=models.CharField(max_length=100, verbose_name="Correo Electrónico")
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad")
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, verbose_name="Compra")

class DetalleVenta(models.Model):
    cantidadProducto = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Cantidad Producto") 
    valorTotalProducto = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total Producto")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")

class Venta(models.Model):
    subTotalVenta= models.PositiveBigIntegerField(validators = [ MinValueValidator ( 1 )], verbose_name="Subtotal Venta")
    fecha= models.DateTimeField('%Y-%m-%d %H:%M:%S')
    porcentajeIva=models.DecimalField(validators=[MinValueValidator(0.0)],decimal_places=1,max_digits=2, verbose_name="Porcentaje IVA")
    totalVenta= models.PositiveBigIntegerField(validators = [ MinValueValidator ( 1 )], verbose_name="Total Venta")
    detalleVenta= models.ForeignKey(DetalleVenta, on_delete=models.CASCADE, verbose_name="Detalle Venta")
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    