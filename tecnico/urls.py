from django.urls import path
from tecnico.views import tecnicos, recuperar_tecnicos, tecnico_crear, tecnico_modificar, tecnicos, tecnicos_eliminar,recuperar_tecnico

urlpatterns = [
    path('',tecnicos,name="tecnico"),
    #Path to ADD tecnico
    path('tecnico_crear',tecnico_crear,name="tecnico_crear"),
    #Path to EDIT tecnico
    path('tecnico_modificar',tecnico_modificar,name="tecnico_modificar"),
    #Path to DELETE tecnico
    path('tecnicos_eliminar/<int:pk>/', tecnicos_eliminar, name="tecnicos_eliminar"),
    #Path to Recuperar tecnicos
    path('tecnicos_recuperar/', recuperar_tecnicos, name="recuperar_tecnicos"),
    path('recuperar_tecnico/<int:pk>/', recuperar_tecnico, name='recuperar_tecnico'),
]