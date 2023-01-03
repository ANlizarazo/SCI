from django.urls import path
from ventas.views import ventas

urlpatterns = [
    path('',ventas,name="ventas"),
]