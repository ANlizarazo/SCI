from django.contrib import admin
from .models import Usuario
# Register your models here.
class UsuarioAdmin (admin.ModelAdmin):
    list_display=("id", "nombres","apellidos","telefono","email")
    search_fields=("rol", "nombres", "apellidos", "numDocumento")
    list_filter=("rol")
    list_per_page =8

admin.site.register(Usuario)
