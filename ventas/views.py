from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from ventas.models import Venta,Usuario, Producto, Cliente
from django.contrib import messages

# se incluyen las siguientes importaciones
from ventas.forms import VentaForm

# Create your views here.   

def ventas (request):
    #importar las ventas desde el modulo admin
    ventas=Venta.objects.all()
    usuarios = Usuario.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    form = VentaForm()
    
    for venta in ventas:
        print(venta.usuario)
        print(venta.cliente)
        print(venta.producto)

    context = {
        'ventas': ventas,
        'usuarios': usuarios,
        'clientes': clientes,
        'productos': productos,
        'form': form,
    }

    return render(request,'ventas/ventas.html', context)

#Function to ADD Venta
def venta_crear(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"¡Venta creada correctamente!")
            return redirect('ventas')
        else:
            messages.error(request, "¡Error al crear venta!")
    context = {
        'form': form,
    }

    return render(request, 'ventas/ventas-crear.html', context)
        


#Function to View Venta data individually
"""def venta_ver(request, venta_id):
    venta = Venta.objects.get( id = venta_id) 
    if venta != None:
        return render(request, "ventas/ventas-modificar.html", {'venta':venta} )
    else:
        return redirect('proveedores/proveedores-ver.html')
"""

def venta_ver(request, pk):
    venta = Venta.objects.get(id = pk)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance = venta)
        if form.is_valid():
            form.save()
            messages.success(request, "venta modificada")
            return redirect('ventas')
        else:
            messages.error(request, "Error al modificar venta")
            print("Error al editar venta")
    else: 
        form = VentaForm(instance = venta)

    return render(request)


#Function to EDIT Venta
def venta_modificar(request, pk):
    venta = Venta.objects.get(id = pk)
    if request.method == "POST":
        form = VentaForm(request.POST, instance = venta)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Venta modificada correctamente!")
            return redirect('ventas')
        else:
            messages.error(request, "¡Error al modificar venta!")
            return redirect('ventas')

    else:
        form = VentaForm(instance = venta)

    context ={
        'form': form
    }

    return render(request, 'ventas/ventas.html', context)

#Function to DELETE Venta
"""def delete_venta(request, venta_id):
    if request.method == "POST":
        venta = Venta.objects.get(id= venta_id)
        venta.delete()
        messages.success(request, "Venta eliminada satisfactoriamente!")
        return redirect('ventas')"""
        
def ventas_eliminar(request, pk):
    venta = Venta.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "Venta eliminada satisfactoriamente!")
    return redirect('ventas') 

#Function to RECUPERAR ventas
def recuperar_ventas(request):
    
    ventas= Venta.objects.all()
    ventas_recuperables = []

    for venta in ventas:
        if venta.estado == '0':
            ventas_recuperables.append(venta)

    context={
        "ventas":ventas_recuperables
    }
    return render(request,'ventas/ventas-recuperar.html',context)

def recuperar(request, pk):
    titulo = 'Recuperar Venta'
    Venta.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "Venta restaurada satisfactoriamente!")
    return redirect('ventas')
