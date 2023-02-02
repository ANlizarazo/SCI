from django.shortcuts import redirect, render
from proveedores.models import Proveedor
from django.http import HttpResponseRedirect
from proveedores.models import Proveedor
from django.contrib import messages

# Create your views here.

def proveedores (request):
    
    #importar los proveedores desde el modulo admin
    proveedores_list=Proveedor.objects.all()

    return render(request,'proveedores/proveedores.html',  {"proveedores": proveedores_list})

#Function to ADD Proveedor
def proveedor_crear(request):
    if request.method=="POST":
        if request.POST.get('nombreEmpresa') \
            and request.POST.get('email') \
            and request.POST.get('telefono') \
            and request.POST.get('direccion') \
            and request.POST.get('modoPago') \
            and request.POST.get('tiempoEntrega') \
            and request.POST.get('transporteIncluido') \
            and request.POST.get('estado') \
            and request.POST.get('material') \
            and request.POST.get('departamento'):
            proveedor= Proveedor()  
            proveedor.nombreEmpresa= request.POST.get('nombreEmpresa')
            proveedor.email= request.POST.get('email')
            proveedor.telefono= request.POST.get('telefono')
            proveedor.direccion= request.POST.get('direccion')
            proveedor.modoPago= request.POST.get('modoPago')
            proveedor.tiempoEntrega= request.POST.get('tiempoEntrega')
            proveedor.transporteIncluido= request.POST.get('transporteIncluido')
            proveedor.estado= request.POST.get('estado')
            proveedor.material= request.POST.get('material')
            proveedor.departamento= request.POST.get('departamento')
            proveedor.save()
            messages.success(request, "Proveedor añadido con éxito!")
            return redirect('proveedores')
        else:
            messages.error(request, "La creación del proveedor ha fallido!")
            return redirect('proveedores')

#Function to View  Proveedor data individually
def proveedor_ver(request, proveedor_id):
    proveedor = Proveedor.objects.get( id = proveedor_id) 
    if proveedor != None:
        return render(request, "proveedores/proveedores-modificar.html", {'proveedor':proveedor} )
    else:
        return redirect('proveedores/proveedores-ver.html')

#Function to EDIT Proveedor
def proveedor_modificar(request):
    if request.method == "POST":
        proveedor = Proveedor.objects.get(id = request.POST.get('id'))
        if proveedor != None:
            proveedor.nombreEmpresa= request.POST.get('nombreEmpresa')
            proveedor.email= request.POST.get('email')
            proveedor.telefono= request.POST.get('telefono')
            proveedor.direccion= request.POST.get('direccion')
            proveedor.modoPago= request.POST.get('modoPago')
            proveedor.tiempoEntrega= request.POST.get('tiempoEntrega')
            proveedor.transporteIncluido= request.POST.get('transporteIncluido')
            proveedor.estado= request.POST.get('estado')
            proveedor.material= request.POST.get('material')
            proveedor.departamento= request.POST.get('departamento')
            proveedor.save()
            messages.success(request, "Proveedor Actualizado con éxito!")
            return HttpResponseRedirect("proveedores/")

#Function to DELETE Proveedor
def delete_proveedor(request, proveedor_id):
    if request.method == "POST":
        proveedor = Proveedor.objects.get(id= proveedor_id)
        proveedor.delete()
        messages.success(request, "Proveedor eliminado satisfactoriamente!")
        return redirect("proveedores")