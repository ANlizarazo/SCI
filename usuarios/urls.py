from django.urls import path
from django.contrib.auth.decorators import login_required
from usuarios.views import CrearUsuario
from . import views

urlpatterns = [
    path('',views.usuarios,name="usuarios"),
    #Path to ADD usuario
    path('crear_usuario/',login_required(CrearUsuario.as_view())),
    #Path to EDIT usuario
    path('usuario_modificar',views.usuario_modificar,name="usuario_modificar"),
    #Path to View usuario data individually
    path('usuarios/usuario_ver/<str:usuario_id>',views.usuario_ver,name="usuario_ver"),
    #Path to DELETE usuario
    path('usuarios/usuarios/delete_usuario/<int:usuario_id>', views.delete_usuario, name='delete_usuario')
]