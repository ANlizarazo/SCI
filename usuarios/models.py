from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="Nombres")
    apellidos=models.CharField(max_length=45, verbose_name="Apellidos")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    class TipoDocumento(models.Model):
        CC='CC', _('Cédula de Ciudadanía')
        CE='CE', _('Cédula de Extranjería')
        PP='PP', _('Pasaporte')    
    class Genero(models.Model):
        FE='F', _('Femenino')
        MA='M', _('Masculino')
        OT='O', _('Otro')
    class Rol(models.Model):
        AD='Admin', _('Administrador')
        EM='Empl', _('Empleado')
    tipoDocumento=models.CharField(max_length=3, choices=TipoDocumento.CC, verbose_name="Tipo de Documento")
    genero=models.CharField(max_length=3, choices=Genero.FE, verbose_name="Género")
    rol=models.CharField(max_length=2, choices=Rol.AD, verbose_name="Rol")
    numDocumento=models.CharField(max_length=50, verbose_name="Número de Documento")
    email=models.CharField(max_length=100, verbose_name="Correo Electrónico")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
