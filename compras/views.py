from django.shortcuts import redirect, render
from compras.models import  DetalleCompra, Proveedor, Producto
from compras.forms import DetalleCompraForm
from django.contrib import messages

# Create your views here.
def compras(request):
        
    detalleCompra = DetalleCompra.objects.all()
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    form= DetalleCompraForm()
    
    for detallecompra in detalleCompra:
        print(detallecompra.producto)
        print(detallecompra.proveedor)
    
    context={
        'detalleCompra':detalleCompra,
        'productos': productos,
        'proveedores': proveedores,
        'form': form,
    }
    return render(request,'compras/compras.html', context)

#Function to ADD compra
def detalle_crear(request):
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Detalle creado correctamente!')
            return redirect(to='compras')
        else:
            messages.error(request, "¡Error al crear detalle!")
            return redirect(to='compras')
    else:
        form = DetalleCompraForm()
    context = {
        'form': form,
    }
    return render(request, 'compras/compras-detalle.html', context)


#Function to View  compra data individually

def compras_ver(request):
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            return redirect('compras')
    else: 
        form = DetalleCompraForm()

    context = {
        'form': form,
    }
    return render(request, 'compras/compras.html', context)  

#Function to EDIT compra

def compras_modificar(request, pk):
    compra = DetalleCompra.objects.get(id = pk)
    if request.method == "POST":
        form = DetalleCompraForm(request.POST, instance = compra)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Compra modificada correctamente!')
            return redirect('compras')
        else:
            messages.error(request, "¡Error al modificar la compra!")
            return redirect('compras')
    else:
        form = DetalleCompraForm( instance = compra)
    
    context = {
        'form': form,
    }

    return render(request, 'compras/compras.html', context)    

#Function to DELETE compra

def compras_eliminar(request, pk):
    compra = DetalleCompra.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "¡Compra eliminada correctamente!")
    return redirect('compras') 



#Function to RECUPERAR compras
def recuperar_compras(request):
    
    compras= DetalleCompra.objects.all()
    compras_recuperables = []

    for compras in compras:
        if compras.estado == '0':
            compras_recuperables.append(compras)

    context={
        "compras":compras_recuperables
    }
    return render(request,'compras/compras-recuperar.html',context)

def recuperar_compra(request, pk):
    titulo = 'Recuperar Compra'
    DetalleCompra.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "¡Compra restaurada correctamente!")
    return redirect('compras')



