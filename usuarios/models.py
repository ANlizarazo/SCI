from django.db import models

# Create your models here.

class Servicio(models.Model):
    observacion= models.TextField(max_lenght=200, verbose_name="Observación")
    fechadeInicio= models.DateField(auto_now=True, verbose_name="Fecha de Inicio")
    fechadeEntrega= models.DateField(auto_now=True, verbose_name="Fecha de Entrega")    
    precio= models.BigIntegerField(validators=[MinValueValidator(0)], default=0, verbose_name="Precio")
    observacionFinal= models.TextField(max_lenght=30050, verbose_name="Orservación Final")
    tipodeservicio=models.charfield(max_lengh=50, verbose_name="Tipo de servicio")
    tecnico=models.CharField(max_length=50, verbose_name="Técnico")


class Usuario(models.Model):
    nombres=models.CharField(max_length=45, verbose_name="Nombres")
    apellidos=models.CharField(max_length=45, verbose_name="Apellidos")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    numDocumento=models.CharField(max_length=50, verbose_name="Número de Documento")
    email=models.CharField(max_length=100, verbose_name="Correo Electrónico")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")

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
    class Estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    tipoDocumento=models.CharField(max_length=3, choices=TipoDocumento.CC, verbose_name="Tipo de Documento")
    genero=models.CharField(max_length=3, choices=Genero.FE, verbose_name="Género")
    rol=models.CharField(max_length=2, choices=Rol.AD, verbose_name="Rol")

    
