from django.urls import path
from proveedores.views import delete_proveedor, proveedor_crear, proveedor_modificar, proveedor_ver, proveedores 

urlpatterns = [
    path('',proveedores,name="proveedores"),
    #Path to ADD Proveedor
    path('proveedor_crear',proveedor_crear,name="proveedor_crear"),
    #Path to EDIT Proveedor
    path('proveedores_modificar',proveedor_modificar,name="proveedor_modificar"),
    #Path to View  Proveedor data individually
    path('proveedores/proveedor_ver/<str:proveedor_id>',proveedor_ver,name="proveedores_ver"),
    #Path to DELETE Proveedor
    path('proveedores/proveedores/delete_proveedor/<int:proveedor_id>', delete_proveedor, name='delete_proveedor'),

]
