from django.urls import path
from tecnico.views import tecnicos
urlpatterns = [
    path('',tecnicos,name="tecnicos"),
]