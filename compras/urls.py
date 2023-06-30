from django.urls import path
from compras.views import compras,compras_crear,compras_modificar,compras_ver, compras_eliminar, recuperar_compras, \
    recuperar_compra, detalle_crear


urlpatterns = [
    path('',compras,name="compras"),
    #Path to ADD Clientes
    path('compras-crear/',compras_crear,name="compras-crear"),
    path('detalle-crear/',detalle_crear,name="detalle-crear"),
    #Path to EDIT Clientes
    path('compras-modificar/<int:pk>',compras_modificar,name="compras-modificar"),
    #Path to View Clientes data individually
    path('compras-ver/<str:compra_id>',compras_ver,name="compras-ver"),
    #Path to DELETE Clientes
    path('compras_eliminar/<int:pk>/', compras_eliminar, name="compras_eliminar"),
    #Path to RESTORE Clientes
    path('compras_recuperar/', recuperar_compras, name="recuperar_compras"),
    path('recuperar/<int:pk>/', recuperar_compra, name='recuperar_compra'),
]

