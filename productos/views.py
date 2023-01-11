from django.shortcuts import render, redirect

from productos.models import Producto

# Create your views here.
def productos(request):
    
    productos= Producto.objects.all()

    context={
        "productos":productos
    }
    return render(request,'productos/productos.html',context)