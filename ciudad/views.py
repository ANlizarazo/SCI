from django.shortcuts import render, redirect
from ciudad.models import Ciudad, Departamento
from ciudad.forms import CiudadForm
from django.contrib import messages

# Create your views here.
def ciudad(request):
    ciudades = Ciudad.objects.all()
    departamentos = Departamento.objects.all()
    form = CiudadForm()

    #for ciudad in ciudad:
        #print(ciudad.departamento.pk)

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
            return redirect(to='ciudad')
        else:
            messages.error(request, "¡Error al crear ciudad!")
            return redirect(to='ciudad')
    else:
        form = CiudadForm()
    context= {
        'form':form,
    }
    return render(request,'ciudad/ciudad-crear.html',context)
