from django.urls import path
from ventas.views import  recuperar_venta, recuperar_ventas, venta_crear, venta_modificar, venta_ver, ventas, ventas_eliminar 

urlpatterns = [
    path('',ventas,name="ventas"),
    #Path to ADD Venta
    path('venta_crear', venta_crear,name="venta_crear"),
    #Path to EDIT Venta
    path('venta_modificar/<int:pk>', venta_modificar,name="venta_modificar"),
    #Path to View Venta data individually
    path('venta_ver/<str:venta_id>',venta_ver,name="venta_ver"),
    #Path to DELETE Venta
    path('ventas_eliminar/<int:pk>/', ventas_eliminar, name="ventas_eliminar"),
    #Path to Recuperar Ventas
    path('ventas_recuperar/', recuperar_ventas, name="recuperar_ventas"),
    path('recuperar_venta/<int:pk>/', recuperar_venta, name='recuperar_venta'),
]
