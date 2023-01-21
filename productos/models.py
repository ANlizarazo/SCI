from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=60, verbose_name="Nombre Categoría", blank=True) 
    descripcion = models.TextField(max_length=300, verbose_name="Descripción")

    def __str__(self)->str:
        return "%s %s" %(self.nombre)  
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Producto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre Producto") 
    precio = models.PositiveBigIntegerField(validators = [ MinValueValidator ( 1 )], verbose_name="Precio")   
    especificaciones = models.TextField(max_length=300, verbose_name="Especificaciones")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    stock = models.BigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Cantidad")
    stockMinimo = models.PositiveSmallIntegerField(validators = [ MinValueValidator ( 5 )], verbose_name="Cantidad Mínima") 
    porcentajeIva=models.DecimalField(validators=[MinValueValidator(0.0)],decimal_places=1,max_digits=2, verbose_name="Porcentaje IVA")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría",null=True)

    def __str__(self)->str:
        return "%s %s" %(self.nombre, self.categoria)  
            
    def __str__(self):
        return "%s | %s"%(self.stock,self.stockMinimo)
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'