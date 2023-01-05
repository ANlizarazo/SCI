from django.db import models

# Create your models here.

class Ventas(models.Model):
    id= models.AutoField(unique= True, primary_key=True)
    subTotalVenta= models.BigIntegerField(max_length=200, verbose_name="subTotalVenta")
    fecha= models.DateField(max_lenght=10, verbose_name="Fecha")
    porcentajeIva= models.BigInt(max_length=10, verbose_name="porcentaje Iva")
    totalVenta= models.BigIntegerField(max_length=200, verbose_name="total Venta")
    DetalleVenta= models.CharField(max_length=200, verbose_name="Detalle Venta")
    Cliente= models.CharField(max_length=20, verbose_name="Cliente")