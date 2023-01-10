from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Venta(models.Model):
    id= models.AutoField(unique= True, primary_key=True , verbose_name="ID Venta")
    subTotalVenta= models.BigIntegerField(max_length=200, verbose_name="Sub Total Venta")
    fecha= models.DateField(auto_now=10, verbose_name="Fecha")
    porcentajeIva= models.BigIntegerField(max_length=10, verbose_name="Porcentaje IVA")
    totalVenta= models.BigIntegerField(max_length=200, verbose_name="Total Venta")
    DetalleVenta= models.CharField(max_length=200, verbose_name="Detalle Venta")
   
class Cliente(models.Model):
    id = models.AutoField (primary_key = True , unique = True, verbose_name = "ID Cliente")
    nombre= models.CharField(max_length=50, verbose_name="Nombre")
    apellido= models.CharField(max_length=50, verbose_name="Apellido")
    rut= models.CharField(unique=True, max_length=20, verbose_name="RUT")
    class TipoDocumento(models.Model):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')    
    tipoDocumento=models.CharField(max_length=3, choices=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numDocumento= models.CharField(unique=True, max_length=20, verbose_name="Número de Documento")
    telefono= models.CharField(max_length=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=50, verbose_name="Dirección")
    email=models.EmailField(max_length=100, verbose_name="Correo Electrónico")
    