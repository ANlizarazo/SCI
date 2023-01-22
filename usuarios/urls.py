from django.urls import path
from usuarios.views import usuarios,usuarios_crear,usuarios_modificar,usuarios_ver
urlpatterns = [
    path('',usuarios,name="usuarios"),
    path('usuarios-crear/',usuarios_crear,name="usuarios-crear"),
    path('usuarios-modificar/',usuarios_modificar,name="usuarios-modificar"),
    path('usuarios-ver/',usuarios_ver,name="usuarios-ver"),
]