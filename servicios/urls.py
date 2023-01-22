from django.urls import path
from servicios.views import servicios,servicios_crear, servicios_modificar, servicios_ver

urlpatterns = [
    path('',servicios,name="servicios"),
    path('servicios-crear/',servicios_crear,name="servicios-crear"),
    path('servicios-modificar/',servicios_modificar,name="servicios-modificar"),
    path('servicios-ver/',servicios_ver,name="servicios-ver")
]