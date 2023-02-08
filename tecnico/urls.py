from django.urls import path
from . import views

urlpatterns = [
    path('',views.tecnicos,name="tecnico"),
    #Path to ADD tecnico
    path('tecnico_crear',views.tecnico_crear,name="tecnico_crear"),
    #Path to EDIT tecnico
    path('tecnico_modificar',views.tecnico_modificar,name="tecnico_modificar"),
    #Path to View tecnico data individually
    path('tecnico/tecnico_ver/<str:tecnico_id>',views.tecnico_ver,name="tecnico_ver"),
    #Path to DELETE tecnico
    path('tecnico/tecnico/delete_tecnico/<int:tecnico_id>', views.delete_tecnico, name='delete_tecnico')
]