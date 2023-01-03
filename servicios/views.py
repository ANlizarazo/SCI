from django.shortcuts import render
from servicios.forms import ServicioForm

from servicios.models import Servicio

# Create your views here.
def servicios(request):

    servicios= Servicio.objects.all()

    context={

    }
    return render(request,'servicios/servicios.html',context)

def servicios_crear(request):

    if request.method=="POST":
        form= ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            print("El proveedor se guardó correctamente")
            return redirect('clientes')
        else:
            print("El proveedor NO se guardó")
    else:
        form= ServicioForm()
    context={
        "form":form
    }
    return render(request,'servicios/servicios-crear.html',context)