from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


# Create your models here.

class Usuario(models.Model):
    nombres=models.CharField(max_length=50, verbose_name="Nombres")
    apellidos=models.CharField(max_length=50, verbose_name="Apellidos")
    telefono=models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Teléfono")
    email=models.CharField(max_length=100, verbose_name="Correo Electrónico")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    class TipoDocumento(models.TextChoices):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')
        OT='OT', _('Otro') 
    class Genero(models.TextChoices):
        FE='F', _('Femenino')
        MA='M', _('Masculino')
        OT='O', _('Otro')
    class Rol(models.TextChoices):
        AD='Admin', _('Administrador')
        EM='Empl', _('Empleado')
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, verbose_name="Tipo de Documento")
    numDocumento=models.CharField(max_length=20, verbose_name="Número de Documento")
    genero=models.CharField(max_length=3, choices=Genero.choices, verbose_name="Género")
    rol=models.CharField(max_length=5, choices=Rol.choices, verbose_name="Rol")
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    foto=models.ImageField(upload_to='images/usuarios', blank=True, default='\static\img\perfil.jpg')

    def __str__(self)->str:
        return "%s %s %s" %(self.nombres, self.apellidos, self.numDocumento)  
    
    class Meta:
        ordering = ['nombres']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
