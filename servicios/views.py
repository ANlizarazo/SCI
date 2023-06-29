from django.shortcuts import redirect, render
from servicios.forms import ServicioForm, ServicioUpdateForm
from django.contrib import messages

from servicios.models import Servicio

# Create your views here.
def servicios(request):

    servicios= Servicio.objects.all()
    form = ServicioForm()
    context={
        "servicios": servicios,
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
            messages.error("¡Error al crear servicio!")

    context={
        "form":form,
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



#Function to EDIT usuario
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

    return render(request, 'servicios/servicios.html', {'form': form})



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
        if servicio.estado != 'Activo':
            servicios_recuperables.append(servicio)

    context={
        "servicios":servicios_recuperables
    }
    return render(request,'servicios/servicios-recuperar.html',context)



def recuperar_ser(request, pk):
    titulo = 'Recuperar Servicio'
    Servicio.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "¡Servicio restaurado correctamente!")
    return redirect('servicios')