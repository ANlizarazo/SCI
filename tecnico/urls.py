from django.urls import path
from tecnico.views import tecnicos,tecnicos_crear, tecnicos_modificar, tecnicos_ver
urlpatterns = [
    path('',tecnicos,name="tecnicos"),
    path('tecnico-crear/',tecnicos_crear,name="tecnico-crear"),
    path('tecnico-ver/',tecnicos_ver,name="tecnico-ver"),
    path('tecnico-modificar/',tecnicos_modificar,name="tecnico-modificar"),
]