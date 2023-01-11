from django.shortcuts import render, redirect

from ventas.models import Venta

# Create your views here.
def ventas(request):

    usuariosventas= Venta.objects.all()

    context={
        "ventas": ventas
    }
    return render(request,'ventas/ventas.html',context)
