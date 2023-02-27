from django.urls import path
from usuarios.views import recuperar, recuperar_usuarios, usuario_crear, usuario_editar, usuario_modificar, usuario_ver, usuarios, usuarios_eliminar

urlpatterns = [
    path('',usuarios,name="usuarios"),
    #Path to ADD usuario
    path('usuario_crear',usuario_crear,name="usuario_crear"),
    #Path to EDIT usuario
    path('usuario_modificar',usuario_modificar,name="usuario_modificar"),
    #Path to View usuario data individually
    path('usuarios/usuario_ver/<str:usuario_id>',usuario_ver,name="usuario_ver"),
    #Path to DELETE usuario
    path('usuarios_eliminar/<int:pk>/', usuarios_eliminar, name="usuarios_eliminar"),
    #Path to Recuperar usuarios
    path('usuarios_recuperar/', recuperar_usuarios, name="recuperar_usuarios"),
    path('recuperar-usuario/<int:pk>/', recuperar, name='recuperar-usuario'),
    path('editar/<int:pk>', usuario_editar, name = 'usuario-editar'),
]