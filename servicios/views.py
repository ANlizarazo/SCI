from django.shortcuts import render, redirect

from servicios.models import Servicio

# Create your views here.
def servicios(request):

    servicios= Servicio.objects.all()

    context={
        "servicios": servicios
    }
    return render(request,'servicios/servicios.html',context)