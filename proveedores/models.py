from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from clientes.models import Ciudad

# Create your models here.
class Departamento(models.Model):
    nombre= models.CharField(max_length=60, verbose_name="Nombre")
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad")
class Material(models.Model):
    nombre= models.CharField(max_length=100, verbose_name="Nombre")
class Proveedor(models.Model):
    nombreEmpresa= models.CharField(max_length=100, verbose_name="Nombre Empresa")
    email= models.CharField(max_length=100, verbose_name="Correo electrónico")
    telefono= models.CharField(max_length=20, verbose_name="Teléfono")
    direccion= models.CharField(max_length=70, verbose_name="Dirección")
    class ModoPago(models.Model):
        EF='EF', _('Efectivo')
        PV='PV', _('Pago Virtual')
        PT='PT', _('Pago con Tarjeta')    
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    class TransporteIncluido(models.TextChoices):
        SI='1', _('Sí')
        NO='0', _('No')
    modoPago=models.CharField(max_length=3, choices=ModoPago.choices, default=ModoPago.EF, verbose_name="Modo de Pago")
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    tiempoEntrega= models.SmallIntegerField(validators=[MinValueValidator(1)], verbose_name="Tiempo Entrega")
    transporteIncluido= models.CharField( max_length=2, choices=TransporteIncluido.choices, verbose_name="Transporte Incluido")
    departamento= models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="Departamento")
    material= models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="Material")
