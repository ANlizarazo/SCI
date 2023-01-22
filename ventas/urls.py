from django.urls import path
from ventas.views import ventas, ventas_crear, ventas_modificar, ventas_ver

urlpatterns = [
    path('',ventas,name="ventas"),
    path('ventas-crear/',ventas_crear,name="ventas-crear"),
    path('ventas-modificar/',ventas_modificar,name="ventas-modificar"),
    path('ventas-ver/',ventas_ver,name="ventas-ver")
]