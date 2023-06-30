from django.urls import path
from categoria.views import categorias, categoria_crear, categoria_modificar, categoria_eliminar, recuperar_categoria, recuperar_cat

urlpatterns = [
    path('', categorias ,name="categorias"),    
    path('categoria-modificar/<int:pk>/', categoria_modificar, name="categoria_modificar"),
    path('categoria_eliminar/<int:pk>/', categoria_eliminar, name="categoria_eliminar"),
    path('categoria-recuperar/', recuperar_categoria, name="recuperar_categoria"),
    path('recuperar_cat/<int:pk>/', recuperar_cat, name='recuperar_cat'),
    path('categoria-crear/', categoria_crear, name="categoria-crear"),
]