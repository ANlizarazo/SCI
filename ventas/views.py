from pyexpat.errors import messages
from django.shortcuts import render, redirect
from ventas.forms import VentaForm
from ventas.models import Venta


# Create your views here.
def ventas(request):

    ventas = Venta.objects.all()

    context = {
        "ventas": ventas
    }
    return render(request, 'ventas/ventas.html', context)


def ventas_ver(request):

    titulo = "Ventas - Ver"
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            return redirect('ventas')
    else:
        form = VentaForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'ventas/ventas-ver.html', context)


def ventas_crear(request):

    titulo = "Ventas - Crear"
    if request.method == 'POST' and 'form-crear' in request.POST:
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            print("La venta se guardó correctamente")
            return redirect('ventas')
        else:
            print("La venta NO se guardó")
    else:
        form = VentaForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'ventas/ventas-crear.html', context)
