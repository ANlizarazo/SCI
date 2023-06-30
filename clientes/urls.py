from django.urls import path
from clientes.views import clientes,clientes_crear,clientes_modificar,clientes_ver, clientes_eliminar, recuperar_clientes, recuperar_cliente


urlpatterns = [
    path('',clientes,name="clientes"),
    #Path to ADD Clientes
    path('clientes-crear/',clientes_crear,name="clientes-crear"),
    #Path to EDIT Clientes
    path('clientes-modificar/<int:pk>',clientes_modificar,name="clientes-modificar"),
    #Path to View Clientes data individually
    path('clientes-ver/<str:cliente_id>',clientes_ver,name="clientes-ver"),
    #Path to DELETE Clientes
    path('clientes_eliminar/<int:pk>/', clientes_eliminar, name="clientes_eliminar"),
    #Path to RESTORE Clientes
    path('clientes_recuperar/', recuperar_clientes, name="recuperar_clientes"),
    path('recuperar/<int:pk>/', recuperar_cliente, name='recuperar_cliente'),
]

