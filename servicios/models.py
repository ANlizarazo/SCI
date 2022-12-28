from django.db import models

# Create your models here.

class Servicios(models.Model):
    tipo= models.CharField(max_lenght=50, verbose_name="Tipo de servicio")
    responsable= models.CharField(max_lenght=50, verbose_name="Persona responsable")
    descripcion= models.CharField(max_lenght=120, verbose_name="Descripción del servicio")


