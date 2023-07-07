from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.defaults import page_not_found
from clientes.models import Cliente
from compras.models import DetalleCompra
from productos.models import Producto
from ventas.models import Venta

def login_view(request):
    titulo="Inicio de Sesión"
    context={
        'titulo':titulo
    }    
    return render(request,'registration/login.html',context)  

@login_required
def inicio(request):
    titulo="Página Principal"
    cantidad_productos= Producto.objects.all().count()
    cantidad_ventas= Venta.objects.all().count()
    cantidad_clientes= Cliente.objects.all().count()
    cantidad_compras= DetalleCompra.objects.all().count()

    labels_stock=[]
    data_stock=[]
    productos= Producto.objects.all().order_by('stock')

    for producto in productos:
        labels_stock.append(producto.nombre)
        data_stock.append(producto.stock)
        
    context={
        'titulo':titulo,
        'cantidad_productos':cantidad_productos,
        'cantidad_ventas':cantidad_ventas,
        'cantidad_clientes':cantidad_clientes,
        'cantidad_compras':cantidad_compras,
        'labels_stock': labels_stock,
        'data_stock':data_stock,
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
def error_404(request,exception):
    context = {}
    return render(request,'error404.html',context) 

def contacto(request):
    context = {}
    return render(request,'partials/contacto.html',context)

def error_500(request,):
    context={
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

