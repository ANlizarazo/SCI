from django.urls import path
from proveedores.views import proveedores,proveedores_crear,proveedores_modificar,proveedores_ver

urlpatterns = [
    path('',proveedores,name="proveedores"),
    path('proveedores-crear/',proveedores_crear,name="proveedores-crear"),
    path('proveedores-modificar/',proveedores_modificar,name="proveedores-modificar"),
    path('proveedores-ver/',proveedores_ver,name="proveedores-ver")
]