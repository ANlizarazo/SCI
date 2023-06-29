from django.contrib import admin
from proveedores.models import Proveedor
# Register your models here.

class ProveedorAdmin (admin.ModelAdmin):
    list_display=("id", "nombreEmpresa","telefono","email")
    search_fields=("nombreEmpresa", "email")
    list_filter=("nombreEmpresa",)
    list_per_page = 8

admin.site.register(Proveedor)

