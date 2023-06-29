from django.contrib import admin
from proveedores.models import Proveedor,Material
# Register your models here.

class ProveedorAdmin (admin.ModelAdmin):
    list_display=("id", "nombreEmpresa","telefono","email","material")
    search_fields=("nombreEmpresa", "email")
    list_filter=("material",)
    list_per_page = 8

admin.site.register(Proveedor)
admin.site.register(Material)
