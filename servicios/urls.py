from django.urls import path
from servicios.views import servicios,servicios_crear, servicios_modificar, servicios_ver, servicios_eliminar, recuperar_servicios, recuperar_ser

urlpatterns = [
    path('',servicios,name="servicios"),
    path('servicios-crear/',servicios_crear,name="servicios-crear"),
    path('servicios-modificar/<int:pk>',servicios_modificar,name="servicios-modificar"),
    path('servicios-ver/',servicios_ver,name="servicios-ver"),
    path('servicios_eliminar/<int:pk>/', servicios_eliminar, name="servicios_eliminar"),
    path('servicios_recuperar/', recuperar_servicios, name="recuperar_servicios"),
    path('recuperar-ser/<int:pk>/', recuperar_ser, name='recuperar-ser'),
]