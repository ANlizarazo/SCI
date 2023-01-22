from django.urls import path
from productos.views import productos,productos_crear, productos_modificar, productos_ver

urlpatterns = [
    path('',productos,name="productos"),
    path('productos-crear/',productos_crear,name="productos-crear"),
    path('productos-modificar/',productos_modificar,name="productos-modificar"),
    path('productos-ver/',productos_ver,name="productos-ver"),
]