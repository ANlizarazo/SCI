from django.urls import path
from compras.views import compras, compras_crear,compras_modificar,compras_ver

urlpatterns = [
    path('',compras,name="compras"),
    path('compras-crear/',compras_crear,name="compras-crear"),
    path('compras-ver/',compras_ver,name="compras-ver"),
    path('compras-modificar/',compras_modificar,name="compras-modificar"),
]