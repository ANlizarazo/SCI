from pyexpat.errors import messages
from django.shortcuts import render, redirect
from ventas.forms import VentaForm, VentaUpdateForm
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


def ventas_modificar(request,pk, *callback_kwargs):
    titulo = "Ventas - Modificar"
    venta = Venta.objects.get(id=pk)
    if request.method == "POST" and 'form-modificar' in request.POST:
        form = VentaForm(request.POST, instance=Venta)
        modal_status = 'show'
        pk_venta = request.POST['pk']
        ## cuerpo del modal ##
        modal_title = f"Modificar {Venta}"
        modal_submit = "Modificar"
        #######################
        tipo = "modificar"
        form_update = VentaUpdateForm(instance=Venta)
        
        venta = Venta.objects.get(id=pk_venta)
        if form.is_valid():
            form.save()
            return redirect('ventas')
        else:
            print("Hubo un error al guardar los cambios")
    else:
        form = VentaForm(instance=Venta)
    context = {
        'titulo': titulo,
        'form': form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_title,
        'pk': pk_venta,
        'tipo': tipo,
        'form_update':form_update
    }
    return render(request, 'ventas/ventas-modificar.html', context)

