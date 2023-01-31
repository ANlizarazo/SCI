from django.urls import path
from . import views

urlpatterns = [
    path('',views.proveedores,name="proveedores"),
    #Path to ADD Proveedor
    path('proveedor_crear',views.proveedor_crear,name="proveedor_crear"),
    #Path to EDIT Proveedor
    path('proveedores_modificar',views.proveedor_modificar,name="proveedor_modificar"),
    #Path to View  Proveedor data individually
    path('proveedores/<str:proveedor_id>',views.proveedor_ver,name="proveedores_ver"),
    #Path to DELETE Proveedor
    path('proveedores/proveedores/delete_proveedor/<int:proveedor_id>', views.delete_proveedor, name='delete_proveedor')

]
