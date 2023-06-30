
from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from productos.models import Producto
from proveedores.models import Proveedor


#Modelos
class DetalleCompra(models.Model):
    fecha= models.DateField(verbose_name="Fecha", auto_now_add=True, editable=False)
    cantidadProducto = models.BigIntegerField(validators = [ MinValueValidator ( 0 )],  verbose_name="Cantidad Producto") 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto",blank=True, null=True)
    class Iva(models.TextChoices):
        BYS='5', _('Bienes y Servicios')
        GR='19', _('General')    
        EX='0', _('Exento')
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')    
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    totalCompra= models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total", blank=True, null=True)
    valorUnidad = models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Producto Unidad")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor",blank=True, null=True)

    def __str__(self)->str:
        return "%s %s %s %s" %(self.id,self.producto,self.fecha)  
    class Meta:
        ordering = ['id']
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


