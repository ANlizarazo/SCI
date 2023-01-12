from django.shortcuts import render, redirect as shortcuts

def login(request):
    titulo="Inicio de Sesión"
    context={
        'titulo':titulo
    }
    return render(request,'index.html',context)    

def inicio(request):
    titulo="Página Principal"
    context={
        'titulo':titulo
    }
    return render(request,'index2.html',context)    

def error404(request):
    titulo="ERROR 404"
    context={
        'titulo':titulo
    }
    return render(request,'error404.html',context)    

def error500(request):
    titulo="ERROR 500"
    context={
        'titulo':titulo
    }
    return render(request,'error500.html',context)   

def perfil(request):
    titulo="Mi Perfil"
    context={
        'titulo':titulo
    }
    return render(request,'perfil.html',context)   