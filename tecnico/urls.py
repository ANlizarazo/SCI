from django.urls import path
from tecnico.views import tecnicos,tecnicos_crear
urlpatterns = [
    path('',tecnicos,name="tecnicos"),
    path('tecnicos-crear/',tecnicos_crear,name="tecnicos-crear"),
]