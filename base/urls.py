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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

from base.views import inicio, error404, error500, perfil

####### Importes para subir imágenes #######
from django.conf import settings
from django.conf.urls.static import static

############################################

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',inicio,name='inicio'),
    path('error404/',error404,name='error404'),    
    path('error500/',error500,name='error500'),
    path('perfil/',perfil,name='perfil'),
    path('usuarios/',include('usuarios.urls')),
    path('ventas/',include('ventas.urls')),
    path('servicios/',include('servicios.urls')),
    path('proveedores/',include('proveedores.urls'), name="proveedores"),
    path('productos/',include('productos.urls')),
    path('compras/',include('compras.urls')),
    path('clientes/',include('clientes.urls')),
    path('tecnicos/',include('tecnico.urls')),
    # --------------------------------------LOGIN--------------------------------------------
    path('logout/',LogoutView.as_view(),name="logout"),
    path('',auth_views.LoginView.as_view(), name='login_view'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset_password_send/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('accounts/',include('django.contrib.auth.urls')),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

