from django.contrib import admin
from .models import Tecnico
# Register your models here.
class TecnicoAdmin (admin.ModelAdmin):
    list_display=("id", "nombres","apellidos","telefono")
    search_fields=("nombres", "apellidos")
    list_filter=("numDocumento")
    list_per_page =8

admin.site.register(Tecnico)