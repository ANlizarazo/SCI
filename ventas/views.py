from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from ventas.models import Venta
from django.contrib import messages

# se incluyen las siguientes importaciones
from django.contrib.auth.models import User
from ventas.forms import VentaForm

# Create your views here.   

def ventas (request):
    
    #importar las ventas desde el modulo admin
    ventas=Venta.objects.all()
    form = VentaForm()

    context = {
        'ventas': ventas,
        'form': form,
    }

    return render(request,'ventas/ventas.html', context)

#Function to ADD Venta
def venta_crear(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            venta = Venta.objects.create_user(request.POST['fecha'], request.POST['usuario'], '123')
            venta.save()
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
def venta_modificar(request):
    if request.method == "POST":
        venta = Venta.objects.get(id = request.POST.get('id'))
        if venta != None:
            venta.subtotalVenta= request.POST.get('subtotalVenta')
            venta.fecha= request.POST.get('fecha')
            venta.porcentajeIva= request.POST.get('porcentajeIva')
            venta.totalVenta= request.POST.get('totalVenta')
            venta.detalleVenta= request.POST.get('detalleVenta')
            venta.cliente= request.POST.get('cliente')
            venta.usuario= request.POST.get('usuario')
            venta.servicio= request.POST.get('servicio')
            venta.estado= request.POST.get('estado')
            venta.save()
            messages.success(request, "La venta ha sido actualizada con éxito!")
            return HttpResponseRedirect('ventas/')

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
