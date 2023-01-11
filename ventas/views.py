from django.shortcuts import render, redirect
from ventas.forms import VentaForm
from ventas.models import Venta


# Create your views here.
def ventas(request):

    ventas= Venta.objects.all()

    context={
        "ventas": ventas
    }
    return render(request,'ventas/ventas.html',context)

def ventas_crear(request):

    if request.method == 'POST':
        form=VentaForm(request.POST)
        if form.is_valid():
            form.save()
            print("La venta se guardó correctamente")
            return redirect('ventas')
        else:
            print("La venta NO se guardó")
    else:
        form=VentaForm()
    context={
        "form":form
    }
    return render(request,'ventas/ventas-crear.html',context)