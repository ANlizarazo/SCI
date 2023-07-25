from django.shortcuts import redirect, render
from servicios.models import Servicio, TipoServicio, Ciudad, Tecnico
from django.contrib import messages

# se incluyen las siguientes importaciones
from servicios.forms import ServicioForm

# Create your views here.
def servicios(request):

    servicios= Servicio.objects.all()
    tiposdeservicios= TipoServicio.objects.all()
    ciudades= Ciudad.objects.all()
    tecnicos = Tecnico.objects.all()
    form = ServicioForm()
    servicioOperacion = []

    for servicio in servicios:
        print(servicio.tipoServicio)
        print(servicio.ciudad)
        print(servicio.tecnico)
        servicio.valorTotal = (int(servicio.valorServicio)*int(servicio.porcentajeIva)/100) + servicio.valorServicio
        servicioOperacion.append(servicio)
    
    context={
        'servicios': servicios,
        'tiposdeservicios': tiposdeservicios,
        'ciudades': ciudades,
        'tecnicos': tecnicos,
        'form': form,
        'servicioOperacion': servicioOperacion,
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
            messages.error(request, "¡Error al modificar servicio!")
            return redirect('servicios')
        
    else:
        form = ServicioForm(instance = servicio)

    context={
        'form': form
    }
    return render(request, 'servicios/servicios.html', context)


#Function to eliminar servicios

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
    servicioOperacion = []

    for servicio in servicios:
        if servicio.estado == '0':
            servicio.valorTotal = (int(servicio.valorServicio)*int(servicio.porcentajeIva)/100) + servicio.valorServicio
            servicios_recuperables.append(servicio)
            servicioOperacion.append(servicio)
        

    context={
        'servicios':servicios_recuperables, 
        'servicioOperacion': servicioOperacion,
    }
    return render(request,'servicios/servicios-recuperar.html',context)



def recuperar_servicio(request, pk):
    titulo = 'Recuperar Servicio'
    Servicio.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "¡Servicio restaurado correctamente!")
    return redirect('servicios')