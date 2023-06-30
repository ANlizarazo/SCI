from django.urls import path
from proveedores.views import proveedores,proveedores_crear,proveedores_modificar,proveedores_ver, proveedores_eliminar, recuperar_proveedores, recuperar_proveedor


urlpatterns = [
    path('',proveedores,name="proveedores"),
    #Path to ADD Clientes
    path('proveedores-crear/',proveedores_crear,name="proveedores-crear"),
    #Path to EDIT Clientes
    path('proveedores-modificar/<int:pk>',proveedores_modificar,name="proveedores-modificar"),
    #Path to View Clientes data individually
    path('proveedores-ver/<str:cliente_id>',proveedores_ver,name="proveedores-ver"),
    #Path to DELETE Clientes
    path('proveedores_eliminar/<int:pk>/', proveedores_eliminar, name="proveedores-eliminar"),
    #Path to RESTORE Clientes
    path('proveedores_recuperar/', recuperar_proveedores, name="recuperar_proveedores"),
    path('recuperar/<int:pk>/', recuperar_proveedor, name='recuperar_proveedor'),

]
