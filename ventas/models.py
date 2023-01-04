from django.db import models

# Create your models here.
class Ventas(models.Model):
    subTotalVenta= models.CharField(max_lenght=50, verbose_name="")
    fechaVenta= models.CharField(max_lenght=50, verbose_name="Fecha")
    porcentajedelIva= models.CharField(unique=True, max_lenght=10, verbose_name="IVA")
    totalVenta= models.CharField(max_lenght=50, verbose_name="Valor total")
    detalleVenta= models.CharField(max_lenght=50, verbose_name="Venta")
    cantidadProducto= models.CharField(max_lenght=50, verbose_name="Cantidad")
    valorTotalProducto= models.CharField(unique=True, max_lenght=10, verbose_name="Valor total")
    cantidadMaterial= models.CharField(unique=True, max_lenght=10, verbose_name="Material")
    valorTotalMaterial= models.CharField(max_lenght=50, verbose_name="Valor total")
    
