from django.shortcuts import redirect, render
from proveedores.forms import ProveedorForm

from proveedores.models import Proveedor

# Create your views here.


def proveedores(request):

    proveedores= Proveedor.objects.all()

    context={
        "proveedores": proveedores
    }
    return render(request,'proveedores/proveedores.html',context)

def proveedores_crear(request):

    if request.method=="POST":
        form= ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            print("El proveedor se guardó correctamente")
            return redirect('clientes')
        else:
            print("El proveedor NO se guardó")
    else:
        form= ProveedorForm()
    context={
        "form":form
    }
    return render(request,'proveedores/proveedores-crear.html',context)