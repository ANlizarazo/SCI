from django.urls import path
from servicios.views import servicios, servicios_crear, servicios_modificar, servicios_ver, servicios_eliminar, recuperar_servicios, recuperar_servicio

urlpatterns = [
    path('',servicios,name="servicios"),
    path('servicios_crear/',servicios_crear,name="servicios_crear"),
    path('servicios_modificar/<int:pk>',servicios_modificar,name="servicios_modificar"),
    path('servicios_ver/<int:pk>',servicios_ver,name="servicios_ver"),
    path('servicios_eliminar/<int:pk>/', servicios_eliminar, name="servicios_eliminar"),
    path('servicios_recuperar/', recuperar_servicios, name="recuperar_servicios"),
    path('recuperar_servicio/<int:pk>/', recuperar_servicio, name='recuperar_servicio'),
]