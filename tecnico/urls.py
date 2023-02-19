from django.urls import path
from tecnico.views import recuperar, recuperar_tecnicos, tecnico_crear, tecnico_modificar, tecnico_ver, tecnicos, tecnicos_eliminar

urlpatterns = [
    path('',tecnicos,name="tecnico"),
    #Path to ADD tecnico
    path('tecnico_crear',tecnico_crear,name="tecnico_crear"),
    #Path to EDIT tecnico
    path('tecnico_modificar',tecnico_modificar,name="tecnico_modificar"),
    #Path to View tecnico data individually
    path('tecnico/tecnico_ver/<str:tecnico_id>',tecnico_ver,name="tecnico_ver"),
    #Path to DELETE tecnico
    path('tecnicos_eliminar/<int:pk>/', tecnicos_eliminar, name="tecnicos_eliminar"),
    #Path to Recuperar tecnicos
    path('tecnicos_recuperar/', recuperar_tecnicos, name="recuperar_tecnicos"),
    path('recuperar/<int:pk>/', recuperar, name='recuperar'),
]