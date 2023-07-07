from django.urls import path
from compras.views import compras,  recuperar_compra, recuperar_compras, detalle_crear, compras_modificar, compras_ver, compras_eliminar 

urlpatterns = [
    path('',compras,name="compras"),
    #Path to ADD Venta
    path('detalle-crear', detalle_crear,name="detalle-crear"),
    #Path to EDIT Venta
    path('compras-modificar/<int:pk>', compras_modificar,name="compras-modificar"),
    #Path to View Venta data individually
    path('compras-ver/<str:compra_id>',compras_ver,name="compras-ver"),
    #Path to DELETE Venta
    path('compras_eliminar/<int:pk>/', compras_eliminar, name="compras_eliminar"),
    #Path to Recuperar Ventas
    path('compras_recuperar/', recuperar_compras, name="recuperar_compras"),
    path('recuperar_compra/<int:pk>/', recuperar_compra, name='recuperar_compra'),
]

