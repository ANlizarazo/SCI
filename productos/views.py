from django.shortcuts import redirect, render
from productos.forms import ProductoForm

from productos.models import Producto

# Create your views here.
def productos(request):
    
    productos= Producto.objects.all()

    context={
        "productos":productos
    }
    return render(request,'productos/productos.html',context)

def productos_crear(request):
    
    titulo="Productos - Crear"
    if request.method == "POST":
        form= ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            print("El producto se guardó correctamente")
            return redirect('productos')
        else:
            print("El producto NO se guardó")
    else:
        form= ProductoForm()
    context={
        'titulo':titulo,
        "form":form
    }
    return render(request,'productos/productos-crear.html',context)