from django.urls import path
from productos.views import productos,productos_crear, productos_modificar, productos_ver,productos_eliminar, recuperar_productos, recuperar_pro

urlpatterns = [
    path('',productos,name="productos"),
    path('productos-crear/', productos_crear,name="productos-crear"),
    path('productos-modificar/<int:pk>/', productos_modificar, name="productos_modificar"),
    path('productos-ver/<int:pk>', productos_ver,name="productos-ver"),
    path('productos_eliminar/<int:pk>/', productos_eliminar, name="productos_eliminar"),
    path('productos_recuperar/', recuperar_productos, name="recuperar_productos"),
    path('recuperar-pro/<int:pk>/', recuperar_pro, name='recuperar_pro'),
]