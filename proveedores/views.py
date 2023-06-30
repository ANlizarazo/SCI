from django.shortcuts import redirect, render
from proveedores.models import Proveedor, Ciudad
from proveedores.forms import ProveedorForm
from django.contrib import messages


#List of proveedor
def proveedores(request):
    
    proveedores= Proveedor.objects.all()
    ciudades= Ciudad.objects.all()
    form = ProveedorForm()
    
    for proveedor in proveedores:
        print(proveedor.ciudad)
    
    context={
        "proveedor":proveedores,
        "ciudad":ciudades,
        'form': form,
    }
    return render(request,'proveedores/proveedores.html',context)


#Funcion para VER proveedores
def proveedores_ver(request):

    titulo = "Proveedor - Ver"
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            return redirect('proveedores')
    else:
        form = ProveedorForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'proveedores/proveedores.html', context)


#Función para CREAR proveedores
def proveedores_crear(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Proveedor creado correctamente!')
            return redirect('proveedores')
        else:
            messages.error(request, "¡Error al crear proveedor!")
            return redirect('proveedores')
    else:
        form = ProveedorForm()
    context = {
        'form': form,
    }
    return render(request, 'proveedores/proveedores-crear.html', context)


#Función para MODIFICAR proveedores
def proveedores_modificar(request, pk):
    proveedor = Proveedor.objects.get(id = pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance = proveedor)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Proveedor guardado correctamente!')
            return redirect('proveedores')
        else:
            messages.success(request,'Error al modificar proveedor')
            messages.error('proveedores')
    else:
        form = ProveedorForm( instance = proveedor)
    
    context = {
        'form': form,
    }

    return render(request, 'proveedores/proveedores.html', context)    


#Función para ELIMINAR proveedores
def proveedores_eliminar(request, pk):
    proveedor= Proveedor.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "¡Proveedor eliminado correctamente!")
    return redirect('proveedores') 


#Function to RECUPERAR proveedor
def recuperar_proveedores(request):
    
    proveedores= Proveedor.objects.all()
    proveedores_recuperables = []

    for proveedor in proveedores:
        if proveedor.estado == '0':
            proveedores_recuperables.append(proveedor)

    context={
        "proveedores":proveedores_recuperables
    }
    return render(request,'proveedores/proveedores-recuperar.html',context)



def recuperar_proveedor(request, pk):
    titulo = 'Recuperar Proveedor'
    Proveedor.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "¡Proveedor restaurado correctamente!")
    return redirect('proveedores')