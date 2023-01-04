from django.db import models

# Create your models here.

class Ventas(models.Model):
    id= models.AutoField(primary_key=True)
    subTotalVenta=models.CharField(max_length=20, verbose_name="subTotalVenta")
    fecha= models.CharField(max_lenght=50, verbose_name="Fecha")
    porcentajeIva=models.CharField(max_length=20, verbose_name="porcentajeIva")
    totalVenta=models.CharField(max_length=20, verbose_name="totalVenta")
    DetalleVenta=models.CharField(max_length=20, verbose_name="DetalleVenta")
    Cliente=models.CharField(max_length=20, verbose_name="Cliente")