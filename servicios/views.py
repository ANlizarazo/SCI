from django.shortcuts import redirect, render
from servicios.forms import ServicioForm
from django.contrib import messages
from servicios.models import Servicio, TipoServicio

# Create your views here.
def servicios(request):

    servicios= Servicio.objects.all()
    tiposdeservicios= TipoServicio.objects.all()
    form = ServicioForm()

    for servicio in servicios:
        print(servicio.tipoServicio)

    context={
        "servicios": servicios,
        "tiposdeservicios": tiposdeservicios,
        "form": form,
    }
    return render(request,'servicios/servicios.html',context)



def servicios_crear(request):
    if request.method == "POST":
        form= ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Servicio creado correctamente!')
            return redirect('servicios')
        else:
            print("El servicio NO se guardó")
            messages.error(request,'¡Error al crear servicio!')
            return redirect('servicios')
    else:
        form = ServicioForm()
    context={
        "form":form,
    }
    return render(request,'servicios/servicios-crear.html',context)


    
def servicios_ver(request):

    titulo = "Servicios - Ver"
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            return redirect('servicios')
    else:
        form = ServicioForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'servicios/servicios.html', context)



#Function to modificar servicios
def servicios_modificar(request, pk):
    servicio = Servicio.objects.get(id = pk)
    if request.method == "POST":
        form = ServicioForm(request.POST, instance = servicio)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Servicio modificado correctamente!")
            return redirect('servicios')
        else:
            messages.error(request, "¡Error al modificar el servicio!")
            print('Error al modificar el servicio')
    else:
        form = ServicioForm(instance = servicio)
    context={
        "form": form
    }
    return render(request, 'servicios/servicios.html', context) 



def servicios_eliminar(request, pk):
    servicio = Servicio.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "¡Servicio eliminado correctamente!")
    return redirect('servicios') 



#Function to RECUPERAR servicios
def recuperar_servicios(request):
    
    servicios= Servicio.objects.all()
    servicios_recuperables = []

    for servicio in servicios:
        if servicio.estado == '0':
            servicios_recuperables.append(servicio)

    context={
        "servicios":servicios_recuperables
    }
    return render(request,'servicios/servicios-recuperar.html',context)



def recuperar_servicio(request, pk):
    titulo = 'Recuperar Servicio'
    Servicio.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "¡Servicio restaurado correctamente!")
    return redirect('servicios')