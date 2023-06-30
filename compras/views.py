from django.shortcuts import redirect, render
from compras.models import Compra, DetalleCompra, Proveedor, Producto
from compras.forms import CompraForm,CompraUpdateForm, DetalleCompraForm
from django.contrib import messages

# Create your views here.
def compras(request):
        
    compras = Compra.objects.all()
    detalleCompra = DetalleCompra.objects.all()
    form= CompraForm()
    form= DetalleCompraForm()
    
    for compra in compras:
        print(compra.detallecompra)
    
    context={
        'detalleCompra':detalleCompra,
        "compras": compras,
        'form': form,
    }
    return render(request,'compras/compras.html', context)

def detalle(request):
    detalleCompra = DetalleCompra.objects.all()
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    form= DetalleCompraForm()

    for detallecompra in detalleCompra:
        print(detallecompra.cantidadProducto)
        print(detallecompra.subtotalCompra) 
        print(detallecompra.porcentajeIva)
        print(detallecompra.totalCompra)
        print(detallecompra.valorTotalProducto)
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
def compras_crear(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Compra creada correctamente!')
            return redirect(to='compras')
        else:
            messages.error(request, "¡Error al crear compra!")
            return redirect(to='compras')
    else:
        form = CompraForm()
    context = {
        'form': form,
    }
    return render(request, 'compras/compras-crear.html', context)

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

def compras_ver(request, pk):
    compra = Compra.objects.get(id = pk)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance =compra)
        if form.is_valid():
            form.save()
            messages.success(request, "compra modificado")
            return redirect('compras')
        else:
            print("Error al editar la compra")
    else: 
        form = CompraForm(instance = compra)
        context = {
        'form': form,
    }
    return render(request, 'compras/compras-ver.html', context)  

#Function to EDIT compra

def compras_modificar(request, pk):
    compra = Compra.objects.get(id = pk)
    if request.method == "POST":
        form = CompraForm(request.POST, instance = compra)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Compra guardada correctamente!')
            return redirect('compras')
        else:
            print('Error al modificar compra')
            messages.error(request, "¡Error al modificar la compra!")
    else:
        form = CompraForm( instance = compra)
    
    context = {
        'form': form,
    }

    return render(request, 'compras/compras-modificar.html', context)    

#Function to DELETE compra

def compras_eliminar(request, pk):
    compra = Compra.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "¡Compra eliminada correctamente!")
    return redirect('compras') 



#Function to RECUPERAR compras
def recuperar_compras(request):
    
    compras= Compra.objects.all()
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
    Compra.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "¡Compra restaurada correctamente!")
    return redirect('compras')



