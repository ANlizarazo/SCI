from django.urls import path
from productos.views import productos

urlpatterns = [
    path('',productos,name="productos"),
]