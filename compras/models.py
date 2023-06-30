
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from productos.models import Producto
from proveedores.models import Proveedor


class DetalleCompra(models.Model):
    cantidadProducto = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], default=0, verbose_name="Cantidad Producto") 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto",null=True)
    subtotalCompra= models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )], default=0, verbose_name="Subtotal Compra")
    class Iva(models.TextChoices):
        BYS='5', _('Bienes y Servicios')
        GR='19', _('General')    
        EX='0', _('Exento')
    porcentajeIva=models.CharField(max_length=3, choices=Iva.choices, default=Iva.GR, verbose_name="IVA") 
    totalCompra= models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Total Compra", default=1, blank=True, null=True)
    valorTotalProducto = models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total Producto")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor",null=True)
    
    def __str__(self)->str:
        return "%s %s %s %s" %(self.id,self.producto,self.cantidadProducto,self.valorTotalProducto)  
    class Meta:
        ordering = ['id']
        verbose_name = 'Detalle Compra'
        verbose_name_plural = 'Detalles de Compras'


class Compra(models.Model):
    fecha= models.DateField(verbose_name="Fecha", auto_now_add=True, editable=False)
    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')    
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

    def __str__(self)->str:
        return "%s %s" %(self.id,self.fecha)  
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'