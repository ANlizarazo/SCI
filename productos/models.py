from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from categoria.models import Categoria

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre Producto") 
    especificaciones = models.TextField(max_length=300, verbose_name="Especificaciones")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría",null=True, blank=True)
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    stock = models.PositiveBigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Stock")
    def __str__(self)->str:
        return "%s - %s" %(self.nombre, self.categoria)  
    """
    @property
    def stock(self):
        from django.db.models import Sum
        from compras.models import DetalleCompra

        aumenta =   DetalleCompra.objects.filter(
            producto = self,
            estado = 1
        ).aggregate(Sum('cantidadProducto'))
        
        return aumenta"""

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'