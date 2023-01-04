from multiprocessing import context 
from django.shortcuts import redirect, render
from servicios.forms import ServicioForm

from servicios.models import Servicio

# Create your views here.
def servicios(request):

    servicios= Servicio.objects.all()

    context={
        "servicios": servicios
    }
    return render(request,'servicios/servicios.html',context)

def servicios_crear(request):

    if request.method=="POST":
        form= ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            print("El servicio se guardó correctamente")
            return redirect('clientes')
        else:
            print("El servicio NO se guardó")
    else:
        form= ServicioForm()
    context={
        "form":form
    }
    return render(request,'servicios/servicios-crear.html',context)