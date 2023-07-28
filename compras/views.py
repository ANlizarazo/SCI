from django.shortcuts import redirect, render
from compras.models import DetalleCompra, Proveedor, Producto
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

# se incluyen las siguientes importaciones
from compras.forms import DetalleCompraForm

@login_required
@permission_required('compras.view_detallecompra')
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
        
def compras_eliminar(request, pk):
    detallecompra = DetalleCompra.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "Compra eliminada satisfactoriamente!")
    return redirect('compras') 

#Function to RECUPERAR compras
def recuperar_compras(request):
    
    detallecompra= DetalleCompra.objects.all()
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
