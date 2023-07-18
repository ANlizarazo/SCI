from django.contrib import admin
from .models import Servicio
from tipodeservicio.models import TipoServicio
# Register your models here.
admin.site.register(Servicio)
admin.site.register(TipoServicio)
