
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from ventas.models import Venta
from django.contrib import messages

# Create your views here.

def ventas (request):
    
    #importar las ventas desde el modulo admin
    ventas_list=Venta.objects.all()

    return render(request,'ventas/ventas.html',  {"ventas": ventas_list})

#Function to ADD Venta
def venta_crear(request):
    if request.method=="POST":
        if request.POST.get('subtotalVenta') \
            and request.POST.get('fecha') \
            and request.POST.get('porcentajeIva') \
            and request.POST.get('totalVenta') \
            and request.POST.get('detalleVenta') \
            and request.POST.get('cliente') \
            and request.POST.get('usuario') \
            and request.POST.get('servicio'):
            venta= Venta()  
            venta.subtotalVenta= request.POST.get('subtotalVenta')
            venta.fecha= request.POST.get('fecha')
            venta.porcentajeIva= request.POST.get('porcentajeIva')
            venta.totalVenta= request.POST.get('totalVenta')
            venta.detalleVenta= request.POST.get('detalleVenta')
            venta.cliente= request.POST.get('cliente')
            venta.usuario= request.POST.get('usuario')
            venta.servicio= request.POST.get('servicio')
            venta.save()
            messages.success(request, "La venta ha sido añadida con éxito!")
            return redirect('ventas')
        else:
            messages.error(request, "La creación de la venta ha fallido!")

#Function to View Venta data individually
def venta_ver(request, venta_id):
    venta = Venta.objects.get( id = venta_id) 
    if venta != None:
        return render(request, "ventas/ventas-modificar.html", {'venta':venta} )
    else:
        return redirect('proveedores/proveedores-ver.html')

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
            venta.save()
            messages.success(request, "La venta ha sido actualizada con éxito!")
            return HttpResponseRedirect('ventas/')

#Function to DELETE Venta
def delete_venta(request, venta_id):
    if request.method == "POST":
        venta = Venta.objects.get(id= venta_id)
        venta.delete()
        messages.success(request, "Venta eliminada satisfactoriamente!")
        return redirect('ventas')