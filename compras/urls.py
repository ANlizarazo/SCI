from django.urls import path
from compras.views import compras

urlpatterns = [
    path('',compras,name="compras"),
]