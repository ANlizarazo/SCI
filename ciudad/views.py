from django.shortcuts import render, redirect
from ciudad.models import Ciudad, Departamento
from ciudad.forms import CiudadForm
from django.contrib import messages

# Create your views here.
def ciudades(request):
    ciudades = Ciudad.objects.all()
    departamentos = Departamento.objects.all()
    form = CiudadForm()

    for ciudad in ciudades:
        print(ciudad.nombre)
        print(ciudad.departamento)

    context = {
        'ciudades':ciudades,
        'departamentos':departamentos,
        'form':form,
    }

    return render(request,'ciudad/ciudad.html',context)


def ciudad_crear(request):
    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Ciudad creada correctamente!')
            return redirect('ciudades')
        else:
            messages.error(request, "¡Error al crear ciudad!")
            return redirect('ciudades')
    else:
        form = CiudadForm()
    context= {
        'form':form,
    }
    return render(request,'ciudad/ciudad-crear.html',context)



def ciudad_eliminar(request, pk):
    ciudad = Ciudad.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "¡Ciudad eliminada satisfactoriamente!")
    return redirect('ciudades') 



#Function to RECUPERAR categorias
def recuperar_ciudades(request):
    
    ciudades= Ciudad.objects.all()
    ciudades_recuperables = []

    for ciudad in ciudades:
        if ciudad.estado == '0':
            ciudades_recuperables.append(ciudad)

    context={
        "ciudades":ciudades_recuperables
    }
    return render(request,'ciudad/ciudad-recuperar.html',context)



def recuperar_ciudad(request, pk):
    titulo = 'Recuperar Ciudad'
    Ciudad.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "¡Ciudad restaurada correctamente!")
    return redirect('ciudades')
