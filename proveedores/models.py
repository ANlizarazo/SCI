from django.db import models

# Create your models here.
class Proveedores(models.Model):
    nombreEmpresa= models.CharField(max_lenght=100, verbose_name="Nombre Empresa")
    email= models.CharField(max_lenght=100, verbose_name="Correo electrónico")
    telefono= models.CharField(max_lenght=20, verbose_name="Teléfono")
    direccion= models.CharField(max_lenght=50, verbose_name="Dirección")
        class ModoPago(models.Model):
        EF='EF', _('Efectivo')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')    
        class Estado(models.Model):
        ACTIVO='', _('Activo')
        INACTIVO='Empl', _('Inactivo')
    
    modoPago=models.CharField(max_length=3, choices=ModoPago.EF, verbose_name="Modo de Pago") 
    rol=models.CharField(max_length=2, choices=Rol.AD, verbose_name="Rol")   
    razonsocial= models.CharField(max_lenght=50, verbose_name="Razón social")
    rut= models.CharField(unique=True, max_lenght=10, verbose_name="Código RUT")
    
    ciudad= models.CharField(max_lenght=50, verbose_name="Ciudad")



    class Devolucion(models.Model):
    fechaDevolucion=models.DateField(auto_now=True,verbose_name="Fecha Devolución")
    observaciones=models.TextField(max_length=200, verbose_name="Observaciones")
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    monto=models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Monto")
    detalleCompra=models.ForeignKey(FacturaDetalleVenta, on_delete=models.CASCADE, verbose_name="Detalle Compra")

  `modoPago` VARCHAR(45) NULL,
  `tiempoEntrega` VARCHAR(45) NULL,
  `transporteIncluido` TINYINT NOT NULL,
  `estado` TINYINT NOT NULL,
  `Departamento_idDepartamento` INT NOT NULL,
  `Material_idMaterial` INT NOT NULL,
