from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def login_view(request):
    titulo="Inicio de Sesión"
    context={
        'titulo':titulo
    }    
    return render(request,'registration/login.html',context)  

@login_required
def inicio(request):
    titulo="Página Principal"
    context={
        'titulo':titulo
    }
    return render(request,'index2.html',context)    
"""
def inicio(request):
    titulo="Página Principal"
    cantidad_productos= Producto.objects.all().count()
    cantidad_clientes= Cliente.objects.all().count()
    cantidad_ventas= Venta.objects.all().count()
    cantidad_compras= cantidad_compra.objects.all().count()
    cantidad_proveedores= cantidad_compra.objects.all().count()
    labels_stock=[]
    data_stock=[]
    productos= Producto.objects.all().order_by('stock')
    for producto in productos:
        labels_stock.append(producto.nombre)
        data_stock.append(producto.stock)
    context={
        'titulo':titulo
        'cantidad_clientes':cantidad_clientes,
        'cantidad_productos':cantidad_productos,
        'cantidad_ventas':cantidad_ventas,
        'cantidad_compras':cantidad_compras,
        'cantidad_proveedores':cantidad_proveedores,
        'labels_stock': labels_stock,
        'data_stock':data_stock,
    }
    return render(request,'index2.html',context)    
"""
def error404(request):
    titulo="ERROR 404"
    context={
        'titulo':titulo,
    }
    return render(request,'error404.html',context)    

def error500(request,):
    titulo="ERROR 500"
    context={
        'titulo':titulo,
    }
    return render(request,'error500.html',context)   

@login_required
def perfil(request):
    titulo="Mi Perfil"
    context={
        'titulo':titulo
    }
    return render(request,'perfil.html',context)   

def logout_user(request):
    logout(request)
    return redirect('login')

