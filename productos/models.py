from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from categoria.models import Categoria

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre Producto") 
    #precio = models.PositiveIntegerField(validators = [MinValueValidator ( 1 )], verbose_name="Precio")   
    especificaciones = models.TextField(max_length=300, verbose_name="Especificaciones")
    # class Categoria(models.TextChoices):
    #     PARQUES = 'Parques', _('Parques')
    #     CERRAMIENTOS = 'Cerramientos', _('Cerramientos')
    #     VARIOS = 'Varios', _('Varios')
    #categoria = models.CharField(max_length=15, choices=Categoria.choices, default=Categoria.VARIOS, verbose_name='Categoria')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría",null=True, blank=True)
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    stock = models.PositiveBigIntegerField(validators = [ MinValueValidator ( 0 )], verbose_name="Stock")
    #stockMinimo = models.PositiveSmallIntegerField(validators = [ MinValueValidator ( 5 )], verbose_name="Cantidad Mínima") 
    #porcentajeIva=models.DecimalField(validators=[MinValueValidator(0.0)],decimal_places=1,max_digits=2, verbose_name="Porcentaje IVA")
    
    #foto=models.ImageField(upload_to='images/productos', blank=True)

    def __str__(self)->str:
        return "%s - %s" %(self.nombre, self.categoria)  
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'