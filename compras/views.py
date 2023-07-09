from django.shortcuts import redirect, render
from compras.models import DetalleCompra, Proveedor, Producto
from django.contrib import messages

# se incluyen las siguientes importaciones
from compras.forms import DetalleCompraForm

# Create your views here.   

def compras (request):
    #importar las compras desde el modulo admin
    detalleCompra= DetalleCompra.objects.all()
    proveedores = Proveedor.objects.all()
    productos = Producto.objects.all()
    form = DetalleCompraForm()
    compraoperacion = []

    for detallecompra in detalleCompra:
        print(detallecompra.proveedor)
        print(detallecompra.producto)
        detallecompra.valorTotal = (int(detallecompra.cantidadProducto)*int(detallecompra.valorUnidad))
        compraoperacion.append(detallecompra)
        
    context = {
        'detalleCompra': detalleCompra,
        'proveedores': proveedores,
        'productos': productos,
        'form': form,
        'compraoperacion': compraoperacion,
    }

    return render(request,'compras/compras.html', context)

#Function to ADD compra
def detalle_crear(request):
    if request.method == 'POST':
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Compra creada correctamente!")
            return redirect('compras')
        else:
            messages.error(request, "¡Error al crear compra!")
            return redirect('compras')
    else:
        form = DetalleCompraForm()
        
    context = {
        'form': form,
    }

    return render(request, 'compras/compras-detalle.html', context)
        

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
            messages.success(request, "¡Compra modificada correctamente!")
            return redirect('compras')
        else:
            messages.error(request, "¡Error al modificar compra!")
            return redirect('compras')

    else:
        form = DetalleCompraForm(instance = compra)

    context ={
        'form': form
    }

    return render(request, 'compras/compras.html', context)


        
def compras_eliminar(request, pk):
    compra = DetalleCompra.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "Compra eliminada satisfactoriamente!")
    return redirect('compras') 

#Function to RECUPERAR compras
def recuperar_compras(request):
    
    compras= DetalleCompra.objects.all()
    compras_recuperables = []
    compraoperacion = []

    for detallecompra in detallecompra:
        if detallecompra.estado == '0':
            detallecompra.valorTotal = (int(detallecompra.cantidadProducto)*int(detallecompra.valorUnidad))
            compras_recuperables.append(detallecompra)
            compraoperacion.append(detallecompra)

    context={
        "compras":compras_recuperables,
        'compraoperacion':compraoperacion,
    }
    return render(request,'compras/compras-recuperar.html',context)

def recuperar_compra(request, pk):
    titulo = 'Recuperar compra'
    DetalleCompra.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "Compra restaurada satisfactoriamente!")
    return redirect('compras')
