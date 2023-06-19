from django.db import models
from django.core.validators import MinValueValidator
from django.utils.formats import get_format
from usuarios.models import Usuario
from proveedores.models import Material, Proveedor




class DetalleCompra(models.Model):
    cantidadMaterial = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Cantidad Material") 
    valorTotalMaterial = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total Material")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario",null=True)
    material= models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Material",null=True)
    
    def _str_(self)->str:
        return "%s %s %s %s" %(self.id,self.usuario,self.cantidadMaterial,self.valorTotalMaterial,self.material)  

    class Meta:
        verbose_name = 'Detalle Compra'
        verbose_name_plural = 'Detalle de Compras'


class Compra(models.Model):
    fecha= models.DateField(verbose_name="Fecha",help_text= "DD/MM/AAA")
    detalleCompra = models.ForeignKey(DetalleCompra, on_delete=models.CASCADE, verbose_name="Detalle Compra",null=True)
    proveedor=models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor",null=True)
    class Estado(models.TextChoices):
        ACTIVO='Activo', ('Activo')
        INACTIVO='Inactivo', ('Inactivo')
    estado=models.CharField(max_length=10, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado", blank=True, null=True)
    

    def _str_(self)->str:
        return "%s %s" %(self.id,self.fecha,self.detalleCompra,self.proveedor,self.estado)  

    class Meta:
        ordering = ['fecha']
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


