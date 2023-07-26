from django.contrib import admin
from .models import Venta
# Register your models here.
class VentaAdmin (admin.ModelAdmin):
    list_display=("id", "fecha","usuario","producto", "valorTotal")
    search_fields=("usuario", "fecha", "producto")
    list_filter=("cliente","usuario","servicio")
    list_per_page = 8

admin.site.register(Venta)