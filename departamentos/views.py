from django.urls import reverse
from django.shortcuts import render, redirect
from departamentos.models import Departamento
from departamentos.forms import DepartamentoForm
from django.contrib import messages

# Create your views here.
def departamento(request):
    departamentos = Departamento.objects.all()
    form = DepartamentoForm()

    context = {
        'departamentos':departamentos,
        'form':form,
    }

    return render(request,'departamentos/departamentos.html',context)

def departamento_crear(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Departamento creado correctamente!')
            return redirect(to='departamentos')
        else:
            messages.error(request, "¡Error al crear departamento!")
            return redirect(to='departamentos')
    else:
        form = DepartamentoForm()
    context= {
        'form':form,
    }
    return render(request,'departamentos/departamentos-crear.html',context)

def departamento_eliminar(request, pk):
    departamento = Departamento.objects.filter(id = pk).update(
        estado = 'Inactivo'
    )
    messages.success(request, "Departamento eliminado satisfactoriamente!")
    return redirect('departamentos') 

#Function to RECUPERAR servicios
def recuperar_departamentos(request):
    
    departamentos= Departamento.objects.all()
    departamentos_recuperables = []

    for departamento in departamentos:
        if departamento.estado != 'Activo':
            departamentos_recuperables.append(departamento)

    context={
        "departamentos":departamentos_recuperables
    }
    return render(request,'departamentos/departamentos-recuperar.html',context)



def recuperar_departamento(request, pk):
    titulo = 'Recuperar departamento'
    Departamento.objects.filter(id = pk).update(
        estado = 'Activo'
    )
    messages.success(request, "Departamento restaurado satisfactoriamente!")
    return redirect('departamentos')