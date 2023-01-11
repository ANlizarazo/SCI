from django.shortcuts import render,redirect

from proveedores.models import Proveedor

# Create your views here.


def proveedores(request):

    proveedores= Proveedor.objects.all()

    context={
        "proveedores": proveedores
    }
    return render(request,'proveedores/proveedores.html',context)
