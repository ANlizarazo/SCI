from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from clientes.models import Ciudad

# Create your models here.
class TipoServicio(models.Model):
    nombreServicio= models.CharField(max_length=50, verbose_name="Nombre de Servicio")
    descripcion= models.CharField(max_length=300, verbose_name="Descripción del Servicio")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')   
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
class Tecnico(models.Model):
    nombres= models.CharField(max_length=45, verbose_name="Nombres")
    apellidos= models.CharField(max_length=45, verbose_name="Apellidos")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")  
    class Genero(models.TextChoices):
        FE='F', _('Femenino')
        MA='M', _('Masculino')
        OT='O', _('Otro')
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    genero=models.CharField(max_length=3, choices=Genero.choices, verbose_name="Género")    
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad")
class Servicio(models.Model):
    observacion= models.CharField(max_length=200, verbose_name="Observaciones")
    fechaInicio= models.DateTimeField('%Y-%m-%d %H:%M:%S', verbose_name="Fecha de Inicio")
    fechaEntrega= models.DateTimeField('%Y-%m-%d %H:%M:%S', verbose_name="Fecha de Entrega")   
    precio= models.PositiveBigIntegerField(validators=[MinValueValidator(1)], verbose_name="Precio")
    observacionFinal= models.CharField(max_length=250, verbose_name="Orservación Final")
    tipodeservicio=models.CharField(max_length=50, verbose_name="Tipo de servicio")
    tecnico=models.CharField(max_length=50, verbose_name="Técnico")
    tipoServicio= models.ForeignKey(TipoServicio, on_delete=models.CASCADE, verbose_name="Tipo de Servicio")
    tecnico= models.ForeignKey(Tecnico, on_delete=models.CASCADE, verbose_name="Técnico")
