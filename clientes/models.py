from django.db import models
from django.utils.translation import gettext_lazy as _
from compras.models import Compra

# Create your models here.

class Ciudad(models.Model):
    nombre= models.CharField(max_length=60, verbose_name="Ciudad")
    
class Cliente(models.Model):
    nombre= models.CharField(max_length=100, verbose_name="Nombre")
    nit= models.CharField(unique=True, max_length=20, verbose_name="NIT")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    email=models.CharField(max_length=100, verbose_name="Correo Electrónico")
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad")
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, verbose_name="Compra")
    

    
    