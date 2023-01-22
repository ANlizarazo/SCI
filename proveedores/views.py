from django.shortcuts import redirect, render
from proveedores.forms import ProveedorForm, ProveedorUpdateForm

from proveedores.models import Proveedor

# Create your views here.


def proveedores(request):

    proveedores= Proveedor.objects.all()

    context={
        "proveedores": proveedores
    }
    return render(request,'proveedores/proveedores.html',context)

def proveedores_ver(request):

    titulo = "Ventas - Ver"
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
    return render(request, 'proveedores/proveedores-ver.html', context)

def proveedores_crear(request):

    titulo="Proveedores - Crear"
    if request.method=="POST" and 'form-proveedor' in request.POST:
        form= ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            print("El proveedor se guardó correctamente")
            return redirect('clientes')
        else:
            print("El proveedor NO se guardó")
    else:
        form= ProveedorForm()
    context={
        'titulo':titulo,
        "form":form
    }
    return render(request,'proveedores/proveedores-crear.html',context)

def proveedores_modificar(request,pk, *callback_kwargs):
    titulo = "Proveedores - Modificar"
    proveedor = Proveedor.objects.get(id=pk)
    if request.method == "POST" and 'form-modificar' in request.POST:
        form = ProveedorForm(request.POST, instance=Proveedor)
        modal_status = 'show'
        pk_proveedor = request.POST['pk']
        ## cuerpo del modal ##
        modal_title = f"Modificar {Proveedor}"
        modal_submit = "Modificar"
        #######################
        tipo = "modificar"
        form_update =ProveedorUpdateForm(instance=Proveedor)
        
        proveedor = Proveedor.objects.get(id=pk_proveedor)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
        else:
            print("Hubo un error al guardar los cambios")
    else:
        form = ProveedorForm(instance=Proveedor)
    context = {
        'titulo': titulo,
        'form': form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_title,
        'pk': pk_proveedor,
        'tipo': tipo,
        'form_update':form_update
    }
    return render(request, 'proveedores/proveedores-modificar.html', context)