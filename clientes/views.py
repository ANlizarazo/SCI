from multiprocessing import context
from django.shortcuts import redirect, render
from clientes.forms import ClienteForm

from clientes.models import Cliente

# Create your views here.


def clientes(request):
    
    clientes= Cliente.objects.all()
    
    context={
        "clientes":clientes
    }
    return render(request,'clientes/clientes.html',context)

def clientes_crear(request):

    if request.method=="POST":
        form= ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            print("El cliente se guardó correctamente")
            return redirect('clientes')
        else:
            print("El cliente NO se guardó")
    else:
        form= ClienteForm()
    context={
        "form":form
    }
    return render(request,'clientes/clientes-crear.html',context)