from django.urls import path
from  departamentos .views import departamento, departamento_crear, departamento_eliminar, recuperar_departamentos, recuperar_departamento

urlpatterns = [
    path('',departamento,name="departamentos"),
    #Path to ADD
    path('departamento-crear',departamento_crear,name="departamento-crear"),
    #Path to Delete
    path('departamento_eliminar/<int:pk>/', departamento_eliminar, name="departamento_eliminar"),
    #Path to RESTORE Clientes
    path('departamentos_recuperar/', recuperar_departamentos, name="recuperar_departamentos"),
    path('recuperar/<int:pk>/', recuperar_departamento, name='recuperar_departamento'),
]
