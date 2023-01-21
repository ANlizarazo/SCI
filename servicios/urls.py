from django.urls import path
from servicios.views import servicios,servicios_crear

urlpatterns = [
    path('',servicios,name="servicios"),
    path('servicios-crear/',servicios_crear,name="servicios-crear"),
]