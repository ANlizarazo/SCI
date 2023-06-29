from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Departamento
from .forms import DepartamentoForm
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