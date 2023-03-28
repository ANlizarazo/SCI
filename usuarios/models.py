from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class UsuarioManager(BaseUserManager):
    def create_user(self, nombres, apellidos, username, email, password = None):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")

        usuario = self.model(
            username = username, 
            email = self.normalize_email(email), 
            nombres = nombres, 
            apellidos = apellidos,
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, nombres, apellidos, username, email, password):
        usuario = self.create_user(
            nombres,
            apellidos,
            username,
            email, 
            password=password,
        )
        usuario.usuario_administrador= True
        usuario.save()
        return usuario
        
class Usuario(AbstractBaseUser):
    username=models.CharField(max_length=50, unique=True, verbose_name="Nombre de Usuario")
    nombres=models.CharField(max_length=50, verbose_name="Nombres")
    apellidos=models.CharField(max_length=50, verbose_name="Apellidos")
    telefono=models.BigIntegerField(validators=[MinValueValidator(0)], blank=True, null=True, verbose_name="Teléfono")
    email=models.CharField(max_length=100, unique=True, verbose_name="Correo Electrónico")
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
    tipoDocumento=models.CharField(max_length=4, blank=True, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    numDocumento=models.CharField(max_length=20, verbose_name="Número de Documento")
    genero=models.BooleanField(max_length=3, blank=True, null=True, choices=Genero.choices, verbose_name="Género")
    rol=models.BooleanField(max_length=5, blank=True, null=True, choices=Rol.choices, verbose_name="Rol")
    estado=models.BooleanField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    foto=models.ImageField(upload_to='images/usuarios', blank=True, null=True, default='\static\img\perfil.jpg')
    usuario_administrador=models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS= ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    #función llamada por el admin de django dando permisos sobre quién puede acceder al admin de  django
    def has_perm(self,perm,obj=None):
        return True 
    
    #función para admin 
    def has_module_perms(self,app_label):
        return True

    #Función que ya vienen definida por el user de Django, verifica si el usuario es administrador
    @property
    def is_staff(self):
        return self.usuario_administrador