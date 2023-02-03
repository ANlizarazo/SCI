from django.urls import path
from . import views

urlpatterns = [
    path('',views.usuarios,name="usuarios"),
    #Path to ADD usuario
    path('usuario_crear',views.usuario_crear,name="usuario_crear"),
    #Path to EDIT usuario
    path('usuario_modificar',views.usuario_modificar,name="usuario_modificar"),
    #Path to View usuario data individually
    path('usuarios/usuario_ver/<str:usuario_id>',views.usuario_ver,name="usuario_ver"),
    #Path to DELETE usuario
    path('usuarios/usuarios/delete_usuario/<int:usuario_id>', views.delete_usuario, name='delete_usuario')
]