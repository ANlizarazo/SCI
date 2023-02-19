from django.contrib import admin
from .models import Tecnico
# Register your models here.
class TecnicoAdmin (admin.ModelAdmin):
    list_display=("id", "nombres","apellidos","telefono","ciudad")
    search_fields=("ciudad", "nombres", "apellidos")
    list_filter=("ciudad")
    list_per_page =8

admin.site.register(Tecnico)