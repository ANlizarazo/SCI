from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from clientes.models import Cliente
from productos.models import Producto
from usuarios.models import Usuario
from servicios.models import Servicio
from tecnico.models import Tecnico

# Create your models here.
class DetalleVenta(models.Model):
    fecha= models.DateField(verbose_name="Fecha", auto_now_add=True, editable=False)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario",blank= True, null=True)
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
        return "%s %s %s %s" %(self.id,self.producto,self.cantidadProducto,self.valorTotalProducto)  
    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalles de Ventas'


class Venta(models.Model):
    
    fecha= models.DateTimeField(verbose_name="Fecha Venta",help_text= "MM/DD/AAAA")
    porcentajeIva=models.DecimalField(validators=[MinValueValidator(0.0)],decimal_places=1,max_digits=20, verbose_name="Porcentaje IVA")
    totalVenta= models.PositiveIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Total Venta")
    detalleVenta= models.ForeignKey(DetalleVenta, on_delete=models.CASCADE, verbose_name="Detalle Venta",null=True)
    
    
    servicio=models.ForeignKey(Servicio, on_delete=models.CASCADE, verbose_name="Servicio",null=True, blank=True)
    tecnico= models.ForeignKey(Tecnico, on_delete=models.CASCADE, verbose_name="Técnico", null=True, blank=True)
      
    

    def __str__(self)->str:
        return "%s %s" %(self.id,self.fecha)  
    
    class Meta:
        ordering = ['fecha']
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'