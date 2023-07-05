from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from clientes.models import Cliente
from productos.models import Producto
from usuarios.models import Usuario

# Create your models here.
class Venta(models.Model):
    fecha= models.DateTimeField(verbose_name="Fecha", auto_now_add=True, editable=False)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente", blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    cantidadProducto = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Cantidad Producto") 
    valorUnidad = models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Unidad")
    
    class ModoPago(models.TextChoices):
        EF='EF', _('Efectivo')
        PV='PV', _('Pago Virtual')
        PT='PT', _('Pago con Tarjeta')
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    class Iva(models.TextChoices):
        BYS='5', _('Bienes y Servicios')
        GR='19', _('General')    
        EX='0', _('Exento')
    modoPago=models.CharField(max_length=3, choices=ModoPago.choices, default=ModoPago.EF, verbose_name="Modo de Pago")
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    porcentajeIva=models.CharField(max_length=3, choices=Iva.choices, default=Iva.GR, verbose_name="IVA")
    valorTotal= models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Valor Total")
    
    def __str__(self)->str:
        return "%s %s %s %s" %(self.id,self.producto,self.id,self.fecha)  
    class Meta:
        ordering = ['fecha']
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalles de Ventas'

