from django.shortcuts import redirect, render
from servicios.forms import ServicioForm, ServicioUpdateForm

from servicios.models import Servicio

# Create your views here.
def servicios(request):

    servicios= Servicio.objects.all()

    context={
        "servicios": servicios
    }
    return render(request,'servicios/servicios.html',context)

def servicios_crear(request):

    titulo="Servicios - Crear"
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
        'titulo':titulo,
        "form":form
    }
    return render(request,'servicios/servicios-crear.html',context)

    
def servicios_ver(request):

    titulo = "Servicios - Ver"
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            return redirect('tecnicos')
    else:
        form = ServicioForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'servicios/servicios-ver.html', context)


def servicios_crear(request):

    titulo = "Servicios - Crear"
    if request.method == 'POST' and 'form-crear' in request.POST:
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            print("El servicio se guardó correctamente")
            return redirect('ventas')
        else:
            print("El Servicio NO se pudo guardar")
    else:
        form = ServicioForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'servicios/servicios-crear.html', context)


def servicios_modificar(request,pk, *callback_kwargs):
    titulo = "Servicios - Modificar"
    Servicio = Servicio.objects.get(id=pk)
    if request.method == "POST" and 'form-modificar' in request.POST:
        form = ServicioForm(request.POST, instance=Servicio)
        modal_status = 'show'
        pk_servicio = request.POST['pk']
        ## cuerpo del modal ##
        modal_title = f"Modificar {Servicio}"
        modal_submit = "Modificar"
        #######################
        tipo = "modificar"
        form_update = ServicioUpdateForm(instance=Servicio)
        
        Servicio = Servicio.objects.get(id=pk_servicio)
        if form.is_valid():
            form.save()
            return redirect('servicios')
        else:
            print("Hubo un error al guardar los cambios")
    else:
        form = ServicioForm(instance=Servicio)
    context = {
        'titulo': titulo,
        'form': form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_title,
        'pk': pk_servicio,
        'tipo': tipo,
        'form_update':form_update
    }
    return render(request, 'servicios/servicios-modificar.html', context)