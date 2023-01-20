from django.contrib import admin
from .models import Proveedor,Material,Departamento,Ciudad
# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Material)
admin.site.register(Departamento)
admin.site.register(Ciudad)