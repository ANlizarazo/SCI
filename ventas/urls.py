from django.urls import path
from ventas.views import ventas, ventas_crear,ventas_ver

urlpatterns = [
    path('',ventas,name="ventas"),
    path('ventas-crear/',ventas_crear,name="ventas-crear"),
    path('ventas-ver/<int:pk>/',ventas_ver,name="ventas-ver")
]