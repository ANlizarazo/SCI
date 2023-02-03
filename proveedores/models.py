from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

from clientes.models import Ciudad


# Create your models here.

class Departamento(models.Model):
    nombre= models.CharField(max_length=60, verbose_name="Nombre")
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad",null=True)

    def __str__(self)->str:
        return "%s %s" %(self.nombre,self.ciudad)  
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

class Material(models.Model):
    nombre= models.CharField(max_length=100, verbose_name="Nombre")

    def __str__(self)->str:
        return "%s" %(self.nombre)  
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'

class Proveedor(models.Model):
    nombreEmpresa= models.CharField(max_length=100, verbose_name="Nombre Empresa")
    email= models.CharField(max_length=100, verbose_name="Correo electrónico")
    telefono= models.CharField(max_length=20, verbose_name="Teléfono")
    direccion= models.CharField(max_length=70, verbose_name="Dirección")
    class ModoPago(models.TextChoices):
        EF='EF', _('Efectivo')
        PV='PV', _('Pago Virtual')
        PT='PT', _('Pago con Tarjeta')    
    class TransporteIncluido(models.TextChoices):
        SI='sí', _('Sí')
        NO='No', _('No')   
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    modoPago=models.CharField(max_length=3, choices=ModoPago.choices, default=ModoPago.EF, verbose_name="Modo de Pago")
    tiempoEntrega= models.SmallIntegerField(validators=[MinValueValidator(1)], verbose_name="Tiempo Entrega") 
    transporteIncluido= models.CharField( max_length=2, choices=TransporteIncluido.choices, verbose_name="Transporte Incluido")
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    material= models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Material",null=True) 
    departamento= models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="Departamento",null=True)

    def __str__(self)->str:
        return "%s %s" %(self.nombreEmpresa,self.material)  
    
    class Meta:
        ordering = ['nombreEmpresa']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'