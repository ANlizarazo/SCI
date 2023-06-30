from django.urls import path
from ciudad.views import ciudad, ciudad_crear

urlpatterns = [
    path('',ciudad,name="ciudad"),
    #Path to ADD ciudad
    path('ciudad-crear/',ciudad_crear,name="ciudad-crear"),
]