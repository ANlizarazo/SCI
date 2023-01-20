from django.urls import path
from proveedores.views import proveedores,proveedores_crear

urlpatterns = [
    path('',proveedores,name="proveedores"),
    path('proveedores-crear/',proveedores_crear,name="proveedores-crear"),
]