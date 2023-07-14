from django.shortcuts import render, redirect
from tipodeservicio.models import TipoServicio
from tipodeservicio.forms import TipoServicioForm
from django.contrib import messages

# Create your views here.

def tiposdeservicios(request):

    tiposdeservicios = TipoServicio.objects.all()
    form = TipoServicioForm()

    for tipodeservicio in tiposdeservicios:
        print(tipodeservicio.nombreServicio)

    context={

        "tiposdeservicios": tiposdeservicios,
        'form': form,
    }
    return render(request,'tipodeservicio/tipodeservicio.html', context)



def tipodeservicio_crear(request):
    titulo = "Tipo de Servicio - Crear"
    if request.method == 'POST':
        form =  TipoServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Tipo de servicio creado correctamente!')
            return redirect('tiposdeservicios')
        else:
            messages.error(request, "¡Error ya existe el tipo de servicio!")
            return redirect('tiposdeservicios')
    else:
        form=TipoServicioForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'servicios/tipodeservicio-crear.html', context)


def tipodeservicio_modificar(request, pk):
    tipodeservicio = TipoServicio.objects.get(id = pk)
    if request.method == "POST":
        form = TipoServicioForm(request.POST, instance = tipodeservicio)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Tipo de servicio modificado correctamente!")
            return redirect('tiposdeservicios')
        else:
            messages.success(request, "¡Error al modificar tipo de servicio!")
            return redirect('tiposdeservicios')
    else:
        form = TipoServicioForm(instance = tipodeservicio)
    
    context ={
        'form': form,
    }

    return render(request, 'tipodeservicio/tipodeservicio.html', context)


def tipodeservicio_eliminar(request, pk):
    tipodeservicio = TipoServicio.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "¡Tipo de servicio eliminado correctamente!")
    return redirect('tiposdeservicios') 



#Function to RECUPERAR categorias
def recuperar_tiposdeservicios(request):
    
    tiposdeservicios= TipoServicio.objects.all()
    tiposdeservicios_recuperables = []

    for tipodeservicio in tiposdeservicios:
        if tipodeservicio.estado != '1':
            tiposdeservicios_recuperables.append(tipodeservicio)

    context={
        "tiposdeservicios":tiposdeservicios_recuperables
    }
    return render(request,'tipodeservicio/tipodeservicio-recuperar.html',context)



def recuperar_tipodeservicio(request, pk):
    titulo = 'Recuperar Tipo de Servicio'
    TipoServicio.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request,'¡Tipo de servicio restaurado correctamente!')
    return redirect('tiposdeservicios')