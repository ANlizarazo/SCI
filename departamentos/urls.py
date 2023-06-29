from django.urls import path
from .views import departamento, departamento_crear

urlpatterns = [
    path('',departamento,name="departamentos"),
    #Path to ADD
    path('departamento-crear',departamento_crear,name="departamento-crear"),
]

