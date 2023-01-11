from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.



class Cliente(models.Model):
    nombre= models.CharField(max_length=100, verbose_name="Nombre")
    apellido= models.CharField(max_length=100, verbose_name="Apellido")
    nit= models.CharField(unique=True, max_length=20, verbose_name="NIT")
    class TipoDocumento(models.Model):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')
        OT= 'Otro', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numDocumento= models.CharField(unique=True, max_length=20, verbose_name="Número de Documento")
    telefono= models.CharField(max_length=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    email=models.EmailField(max_length=100, verbose_name="Correo Electrónico")
    

    
    