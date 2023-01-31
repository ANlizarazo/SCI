from django.contrib import admin
from .models import Venta,DetalleVenta
# Register your models here.
class VentaAdmin (admin.ModelAdmin):
    list_display=("id", "detalleVenta","fecha","cliente","usuario")
    search_fields=("detalleVenta", "fecha")
    list_filter=("cliente","usuario","servicio")
    list_per_page = 8


admin.site.register(Venta)
admin.site.register(DetalleVenta)