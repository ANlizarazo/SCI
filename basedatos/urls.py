from django.urls import path
from basedatos.views import basedatos, respaldar_base_datos, recuperar_base_datos 

urlpatterns = [ 
    path('', basedatos, name = 'basedatos'),
    path('respaldar_base_datos/', respaldar_base_datos, name = 'respaldarBaseDatos'),
    path('recuperar_base_datos/', recuperar_base_datos, name = 'recuperarBaseDatos')
]