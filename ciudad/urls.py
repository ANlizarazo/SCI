from django.urls import path
from ciudad.views import ciudad_eliminar, ciudades, ciudad_crear, recuperar_ciudad, recuperar_ciudades

urlpatterns = [
    path('',ciudades,name="ciudades"),
    #Path to ADD ciudad
    path('ciudad-crear/',ciudad_crear,name="ciudad-crear"),
    path('ciudad_eliminar/<int:pk>/', ciudad_eliminar, name="ciudad_eliminar"),
    path('ciudades_recuperar/', recuperar_ciudades, name="recuperar_ciudades"),
    path('recuperar_ciudad/<int:pk>/', recuperar_ciudad, name='recuperar_ciudad'),
]