from django.urls import path
from productos.views import productos,
productos_crear,productos_buscar,productos modificar,productos_listar

urlpatterns = [
    path('producto/',productos,name="productos"),
    path('producto-crear/',productos_crear,name="productos-crear"),
    path('producto-buscar/',productos_buscar,name="productos-buscar"),
    path('producto-modificar/',productos_modificar,name="productos-modificar")
    path('producto-editar/<int:pk>/',productos_editar,name="productos-editar"),
    path('producto-eliminar/<int:pk>/',productos_eliminar,name="productos-eliminar"),

]