from django.urls import path
from . import views

urlpatterns = [
    path('',views.ventas,name="ventas"),
    #Path to ADD Venta
    path('venta_crear',views.venta_crear,name="venta_crear"),
    #Path to EDIT Venta
    path('venta_modificar',views.venta_modificar,name="venta_modificar"),
    #Path to View Venta data individually
    path('ventas/venta_ver/<str:venta_id>',views.venta_ver,name="venta_ver"),
    #Path to DELETE Venta
    path('ventas/ventas/delete_venta/<int:venta_id>', views.delete_venta, name='delete_venta')

]
