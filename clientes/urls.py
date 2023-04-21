from django.urls import path
from clientes.views import clientes,clientes_crear,clientes_modificar,clientes_ver, ciudad_crear


urlpatterns = [
    path('',clientes,name="clientes"),
    path('clientes-crear/',clientes_crear,name="clientes-crear"),
    path('clientes-modificar/',clientes_modificar,name="clientes-modificar"),
    path('clientes-ver/',clientes_ver,name="clientes-ver"),
    path('clientes-ciudad', ciudad_crear, name='ciudad-crear')
]