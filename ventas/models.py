from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from productos.models import Producto
from clientes.models import Ciudad
from compras.models import Compra


# Create your models here.

class Cliente(models.Model):
    nombres= models.CharField(max_length=50, verbose_name="Nombres")
    apellidos= models.CharField(max_length=50, verbose_name="Apellidos")
    nit= models.CharField(unique=True, max_length=20, verbose_name="NIT")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    email=models.CharField(max_length=100, verbose_name="Correo Electrónico")
    class TipoDocumento(models.Model):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')    
    tipoDocumento=models.CharField(max_length=3, choices=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numDocumento= models.CharField(unique=True, max_length=20, verbose_name="Número de Documento")
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad")
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, verbose_name="Compra")
class DetalleVenta(models.Model):
    cantidadProducto = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Cantidad Material") 
    valorTotalProducto = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total Material")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")

class Venta(models.Model):
    subTotalVenta= models.BigIntegerField(max_length=200, verbose_name="Sub Total Venta")
    fecha= models.DateField(auto_now=True, verbose_name="Fecha")
    porcentajeIva=models.DecimalField(validators=[MinValueValidator(0.0)],decimal_places=1,max_digits=2, verbose_name="Porcentaje IVA")
    totalVenta= models.BigIntegerField(max_length=200, verbose_name="Total Venta")
    detalleVenta= models.ForeignKey(DetalleVenta, on_delete=models.CASCADE, verbose_name="Detalle Venta")
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    