"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import index
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

from base.views import cambioExitoso, correoEnviado, formRecuperacion, inicio, login, error404, error500, nuevaContraseña, perfil




urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/',logout_user,name="logout"),
    path('',auth_views.LoginView.as_view(), name='login'),
    path('recuperacion/',formRecuperacion,name='recuperacion'),
    path('correoenviado/',correoEnviado,name='correoenviado'),
    path('nuevacontraseña/',nuevaContraseña,name='nuevacontraseña'),
    path('cambioexitoso/',cambioExitoso,name='cambioexitoso'),

    path('inicio/',inicio,name='inicio'),
    path('error404/',error404,name='error404'),    
    path('error500/',error500,name='error500'),
    path('perfil/',perfil,name='perfil'),
    path('usuarios/',include('usuarios.urls')),
    path('ventas/',include('ventas.urls')),
    path('servicios/',include('servicios.urls')),
    path('proveedores/',include('proveedores.urls')),
    path('productos/',include('productos.urls')),
    path('compras/',include('compras.urls')),
    path('clientes/',include('clientes.urls')),
    path('tecnicos/',include('tecnico.urls'))
    
]
