from django.shortcuts import redirect, render
from clientes.forms import ClienteForm, ClienteUpdateForm, CiudadForm
from clientes.models import Cliente
from clientes.models import Ciudad
from django.contrib import messages

#Lista de clientes
def clientes(request):
    
    clientes= Cliente.objects.all()
    form = ClienteForm()
    formCiudad = CiudadForm()
    
    context={
        "clientes":clientes,
        'form': form,
        'formCiudad': formCiudad
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
    else:
        form = ClienteForm()
        
    context = {
        'form': form,
    }

    return render(request, 'clientes/clientes-crear.html', context)


#Función para MODIFICAR clientes
def clientes_modificar(request, pk):
    cliente = Cliente.objects.get(id = pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance = cliente)
        if form.is_valid():
            form.save()
            
            return redirect('clientes')
        else:
            print('Error al editar al cliente')
    else:
        form = ClienteForm(instance = cliente)

    return render(request, 'tecnico/tecnico.html', {'form': form})    


#Función para ELIMINAR clientes
def clientes_eliminar(request, pk):
    cliente = Cliente.objects.filter(id = pk).update(
        estado = '0'
    )

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
    
    return redirect('clientes')