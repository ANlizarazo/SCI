from django.urls import path
from compras.views import recuperar, recuperar_compras, compras_crear, compras_modificar, \
    compras_ver, compras, compras_eliminar

urlpatterns = [
    path('',compras,name="compras"),
    path('compras-crear/',compras_crear,name="compras-crear"),
    path('compras-modificar/<int:pk>',compras_modificar,name="compras-modificar"),
    path('compras-ver/',compras_ver,name="compras-ver"),
    path('compras_eliminar/<int:pk>/', compras_eliminar, name="compras_eliminar"),
    path('compras_recuperar/', recuperar_compras, name="recuperar_compras"),
    path('recuperar/<int:pk>/', recuperar, name='recuperar_compra'),
]