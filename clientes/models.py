from django.db import models
from django.utils.translation import gettext_lazy as _
from compras.models import Compra

# Create your models here.

class Ciudad(models.Model):
    nombre= models.CharField(max_length=60, verbose_name="Ciudad")
    
class Cliente(models.Model):
    nombres= models.CharField(max_length=50, verbose_name="Nombres")
    apellidos= models.CharField(max_length=50, verbose_name="Apellidos")
    nit= models.CharField(unique=True, max_length=20, verbose_name="NIT")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    email=models.CharField(max_length=100, verbose_name="Correo Electrónico")
    class TipoDocumento(models.Model):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')    
    tipoDocumento=models.CharField(max_length=3, choices=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numDocumento= models.CharField(unique=True, max_length=20, verbose_name="Número de Documento")
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad")
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, verbose_name="Compra")
    

    
    