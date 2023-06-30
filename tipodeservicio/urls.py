from django.urls import path
from tipodeservicio.views import tiposdeservicios, tipodeservicio_crear, tipodeservicio_modificar, tipodeservicio_eliminar, recuperar_tiposdeservicios, recuperar_tipodeservicio

urlpatterns = [
    path('', tiposdeservicios , name="tiposdeservicios"),        
    path('tipodeservicio-crear/', tipodeservicio_crear, name="tipodeservicio-crear"),
    path('tipodeservicio-modificar/<int:pk>/', tipodeservicio_modificar, name="tipodeservicio_modificar"),
    path('tipodeservicio_eliminar/<int:pk>/', tipodeservicio_eliminar, name="tipodeservicio_eliminar"),
    path('tipodeservicio_recuperar/', recuperar_tiposdeservicios, name="recuperar_tiposdeservicios"),
    path('recuperar_tipodeservicio/<int:pk>/', recuperar_tipodeservicio, name='recuperar_tipodeservicio'),
]