from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Create your models here.
class Ciudad(models.Model):
    nombre= models.CharField(max_length=60, verbose_name="Nombre")

    def __str__(self)->str:
        return "%s %s" %(self.nombre)  
    
    class Meta:
        ordering = ['nombre']
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

class Tecnico(models.Model):
    nombres= models.CharField(max_length=50, verbose_name="Nombres")
    apellidos= models.CharField(max_length=50, verbose_name="Apellidos")
    telefono= models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Teléfono")  
    class Genero(models.TextChoices):
        FE='F', _('Femenino')
        MA='M', _('Masculino')
        OT='O', _('Otro')
    class TipoDocumento(models.TextChoices):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')
        OT='OT', _('Otro') 
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    genero=models.CharField(max_length=3, choices=Genero.choices, verbose_name="Género")    
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, verbose_name="Tipo de Documento")
    numDocumento=models.CharField(max_length=20, unique=True, verbose_name="Número de Documento")
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad",null=True)
    
    def __str__(self)->str:
        return "%s %s" %(self.nombres, self.apellidos, self.numDocumento)  
    
    class Meta:
        ordering = ['nombres']
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'