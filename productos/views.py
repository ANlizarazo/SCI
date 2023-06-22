from django.shortcuts import redirect, render
from productos.forms import ProductoForm
from django.contrib import messages
from productos.models import Producto, Categoria

# Create your views here.
def productos(request):
    
    productos= Producto.objects.all()
    categorias = Categoria.objects.all()
    form = ProductoForm()

    for producto in productos:
        print(producto.categoria.pk)

    context={
        "productos": productos,
        "categorias": categorias,
        'form': form,
        
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
    if request.method == 'POST':
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




#Function to EDIT Producto
def productos_modificar(request, pk):
    producto = Producto.objects.get(id = pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance = producto)
        if form.is_valid():
            form.save()
            
            return redirect('productos')
        else:
            print('Error al editar el producto')
    else:
        form = ProductoForm(instance = producto)

    return render(request, 'productos/productos.html', {'form': form})





def productos_eliminar(request, pk):
    producto = Producto.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "Producto eliminado satisfactoriamente!")
    return redirect('productos') 



#Function to RECUPERAR productos
def recuperar_productos(request):
    
    productos= Producto.objects.all()
    productos_recuperables = []

    for producto in productos:
        if producto.estado != '1':
            productos_recuperables.append(producto)

    context={
        "productos":productos_recuperables
    }
    return render(request,'productos/productos-recuperar.html',context)



def recuperar_pro(request, pk):
    titulo = 'Recuperar Producto'
    Producto.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "Producto restaurado satisfactoriamente!")
    return redirect('productos')




# def productos_modificar(request,pk, *callback_kwargs):
#     titulo = "Productos - Modificar"
#     producto = Producto.objects.get(id=pk)
#     if request.method == "POST" and 'form-modificar' in request.POST:
#         form = ProductoForm(request.POST, instance=Producto)
#         modal_status = 'show'
#         pk_producto = request.POST['pk']
#         ## cuerpo del modal ##
#         modal_title = f"Modificar {Producto}"
#         modal_submit = "Modificar"
#         #######################
#         tipo = "modificar"
#         form_update = ProductoUpdateForm(instance=Producto)
        
#         producto = Producto.objects.get(id=pk_producto)
#         if form.is_valid():
#             form.save()
#             return redirect('productos')
#         else:
#             print("Hubo un error al guardar los cambios")
#     else:
#         form = ProductoForm(instance=Producto)
#     context = {
#         'titulo': titulo,
#         'form': form,
#         'modal_status':modal_status,
#         'modal_submit': modal_submit,
#         'modal_title': modal_title,
#         'pk': pk_producto,
#         'tipo': tipo,
#         'form_update':form_update
#     }
#     return render(request, 'servicios/servicios-modificar.html', context)