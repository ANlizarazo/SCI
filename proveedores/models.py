from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Proveedor(models.Model):
    nombreEmpresa= models.CharField(max_length=100, verbose_name="Nombre Empresa")
    email= models.CharField(max_length=100, verbose_name="Correo electrónico")
    telefono= models.CharField(max_length=20, verbose_name="Teléfono")
    direccion= models.CharField(max_length=50, verbose_name="Dirección")
    class ModoPago(models.Model):
        EF='EF', _('Efectivo')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')    
    modoPago=models.CharField(max_length=3, choices=ModoPago.EF, verbose_name="Modo de Pago") 
    class Rol(models.TextChoices):
        AD='Admin', _('Administrador')
        EM='Empl', _('Empleado')
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    rol=models.CharField(max_length=2, choices=Rol.AD, verbose_name="Rol")
    razonsocial= models.CharField(max_length=50, verbose_name="Razón social")
    rut= models.CharField(unique=True, max_length=10, verbose_name="Código RUT")
    ciudad= models.CharField(max_length=50, verbose_name="Ciudad")
    
    """class Devolucion(models.Model):
    fechaDevolucion=models.DateField(auto_now=True,verbose_name="Fecha Devolución") 
    observacion=models.TextField(max_length=200, verbose_name="Observaciones")"""
