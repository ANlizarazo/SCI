from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from clientes.models import Cliente
from productos.models import Producto
from usuarios.models import Usuario

# Create your models here.
class DetalleVenta(models.Model):
    cantidadProducto = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Cantidad Producto") 
    valorTotalProducto = models.PositiveBigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total Producto")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto",null=True)
    
    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalles de Ventas'


class Venta(models.Model):
    subTotalVenta= models.PositiveBigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Subtotal Venta")
    fecha= models.DateTimeField(verbose_name="Fecha Venta")
    porcentajeIva=models.DecimalField(validators=[MinValueValidator(0.0)],decimal_places=1,max_digits=20, verbose_name="Porcentaje IVA")
    totalVenta= models.PositiveBigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Total Venta")
    detalleVenta= models.ForeignKey(DetalleVenta, on_delete=models.CASCADE, verbose_name="Detalle Venta",null=True)
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente",null=True)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario",null=True)

    def __str__(self)->str:
        return "%s" %(self.fecha)  
    
    class Meta:
        ordering = ['fecha']
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'