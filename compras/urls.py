from django.urls import path
from compras.views import compras, compras_crear

urlpatterns = [
    path('',compras,name="compras"),
    path('compras-crear/',compras_crear,name="compras-crear"),
]