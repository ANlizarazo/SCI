from django.urls import path
from proveedores.views import proveedores

urlpatterns = [
    path('',proveedores,name="proveedores"),
]