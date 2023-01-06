from django.db import models

# Create your models here.

class Servicio(models.Model):
    observacion= models.TextField(max_length=200, verbose_name="Observaciones")
    fechadeInicio= models.DateField(max_length=9, verbose_name="Fecha de Inicio")
    fechadeEntrega= models.DateField(max_length=9, verbose_name="Fecha de Entrega")    
    precio= models.BigIntegerField(max_length=100, verbose_name="Precio")
    observacionFinal= models.TextField(max_length=250, verbose_name="Orservación Final")
    tipodeservicio=models.CharField(max_length=50, verbose_name="tipo de servicio")
    tecnico=models.CharField(max_length=50, verbose_name="Técnico")