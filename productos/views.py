from django.shortcuts import redirect, render
from productos.forms import ProductoForm, ProductoUpdateForm

from productos.models import Producto

# Create your views here.
def productos(request):
    
    productos= Producto.objects.all()

    context={
        "productos":productos
    }
    return render(request,'productos/productos.html',context)
    
def productos_ver(request):

    titulo = "Productos - Ver"
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            return redirect('productos')
    else:
        form = ProductoForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'productos/productos-ver.html', context)


def productos_crear(request):

    titulo = "Productos - Crear"
    if request.method == 'POST' and 'form-crear' in request.POST:
        form =  ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            print("El Producto se guardó correctamente")
            return redirect('productos')
        else:
            print("El Producto NO se pudo guardar")
    else:
        form = ProductoForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'productos/productos-crear.html', context)


def productos_modificar(request,pk, *callback_kwargs):
    titulo = "Productos - Modificar"
    producto = Producto.objects.get(id=pk)
    if request.method == "POST" and 'form-modificar' in request.POST:
        form = ProductoForm(request.POST, instance=Producto)
        modal_status = 'show'
        pk_producto = request.POST['pk']
        ## cuerpo del modal ##
        modal_title = f"Modificar {Producto}"
        modal_submit = "Modificar"
        #######################
        tipo = "modificar"
        form_update = ProductoUpdateForm(instance=Producto)
        
        producto = Producto.objects.get(id=pk_producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
        else:
            print("Hubo un error al guardar los cambios")
    else:
        form = ProductoForm(instance=Producto)
    context = {
        'titulo': titulo,
        'form': form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_title,
        'pk': pk_producto,
        'tipo': tipo,
        'form_update':form_update
    }
    return render(request, 'servicios/servicios-modificar.html', context)