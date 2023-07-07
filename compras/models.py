from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from productos.models import Producto
from proveedores.models import Proveedor


#Modelos
class DetalleCompra(models.Model):
    fecha= models.DateTimeField(verbose_name="Fecha", auto_now_add=True, editable=False, null=True)
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor", blank=True, null=True)
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    cantidadProducto = models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )],  verbose_name="Cantidad Producto") 
    valorUnidad = models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Unidad")
    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')    

    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    valorTotal= models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )], blank=True, null=True, verbose_name="Valor Total")
    
    def __str__(self)->str:
        return "%s %s %s %s" %(self.id,self.producto,self.id,self.fecha)    
    
    class Meta:
        ordering = ['fecha']
        verbose_name = 'Detalle Compra'
        verbose_name_plural = 'Detalles de Compras'


