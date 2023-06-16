from django.urls import path
from clientes.views import clientes,clientes_crear,clientes_modificar,clientes_ver, clientes_eliminar, recuperar_clientes, recuperar_cliente


urlpatterns = [
    path('',clientes,name="clientes"),
    path('clientes-crear/',clientes_crear,name="clientes-crear"),
    path('clientes-modificar/<int:pk>',clientes_modificar,name="clientes-modificar"),
    path('clientes-ver/<str:cliente_id>',clientes_ver,name="clientes-ver"),
    path('clientes_eliminar/<int:pk>/', clientes_eliminar, name="clientes_eliminar"),
    path('clientes_recuperar/', recuperar_clientes, name="recuperar_clientes"),
    path('recuperar/<int:pk>/', recuperar_cliente, name='recuperar_cliente'),
]

