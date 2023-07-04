from django.shortcuts import redirect, render
from clientes.forms import ClienteForm, ClienteUpdateForm
from clientes.models import Cliente, Ciudad
from django.contrib import messages
from django.forms import ValidationError

#Lista de clientes
def clientes(request):
    
    clientes= Cliente.objects.all()
    ciudades= Ciudad.objects.all()
    form = ClienteForm()
    
    for cliente in clientes:
        print(cliente.ciudad)
        print(cliente.nombreEmpresa)

    context={
        "clientes":clientes,
        "ciudades":ciudades,
        'form': form,
    }
    return render(request,'clientes/clientes.html',context)


#Funcion para VER clientes
def clientes_ver(request):

    titulo = "Clientes - Ver"
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            return redirect('clientes')
    else:
        form = ClienteForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'clientes/clientes-ver.html', context)


#Función para CREAR clientes
def clientes_crear(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Cliente creado correctamente!')
            return redirect('clientes')
        else:
            messages.error(request, "¡Error al crear cliente!")
            return redirect('clientes')
    else:
        form = ClienteForm()
    context = {
        "form": form
    }
    return render(request, 'clientes/clientes-crear.html', context)


#Función para MODIFICAR clientes
def clientes_modificar(request, pk):
    cliente = Cliente.objects.get(id = pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance = cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Cliente modificado correctamente!")
            return redirect('clientes')
        else:
            messages.error(request, "¡Error al modificar el cliente!")
            return redirect('clientes')
    else:
        form = ClienteForm(instance = cliente)
    
    context ={
        'form': form,
    }

    return render(request, 'clientes/clientes.html', context)




#Función para ELIMINAR clientes
def clientes_eliminar(request, pk):
    cliente = Cliente.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "¡Cliente eliminado correctamente!")
    return redirect('clientes') 


#Function to RECUPERAR cliente
def recuperar_clientes(request):
    
    clientes= Cliente.objects.all()
    clientes_recuperables = []

    for cliente in clientes:
        if cliente.estado == '0':
            clientes_recuperables.append(cliente)

    context={
        "clientes":clientes_recuperables
    }
    return render(request,'clientes/clientes-recuperar.html',context)



def recuperar_cliente(request, pk):
    titulo = 'Recuperar Cliente'
    Cliente.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "¡Cliente restaurado correctamente!")
    return redirect('clientes')