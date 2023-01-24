from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.defaults import page_not_found

def login(request):
    titulo="Inicio de Sesión"
    context={
        'titulo':titulo
    }
    return render(request,'index.html',context)  

def formRecuperacion(request):
    titulo="Recupera tu Contraseña"
    context={
        'titulo':titulo
    }
    return render(request,'registration/formrecuperacion.html',context)

def correoEnviado(request):
    titulo="Correo de Recuperación Enviado"
    context={
        'titulo':titulo
    }
    return render(request,'registration/correoenviado.html',context)

def nuevaContraseña(request):
    titulo="Crea tu Nueva Contraseña"
    context={
        'titulo':titulo
    }
    return render(request,'registration/nuevacontraseña.html',context)

def cambioExitoso(request):
    titulo="Contraseña Cambiada Correctamente"
    context={
        'titulo':titulo
    }
    return render(request,'registration/cambioexitoso.html',context)

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
        'labels_stock': labels_stock,
        'data_stock':data_stock,
    }
    return render(request,'index2.html',context)    
"""
def error404(request, exception):
    titulo="ERROR 404"
    context={
        'titulo':titulo
    }
    return page_not_found(request,'error404.html',context)    

def error500(request):
    titulo="ERROR 500"
    context={
        'titulo':titulo
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