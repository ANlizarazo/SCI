from django.shortcuts import render, redirect as shortcuts

def login(request):
    context={
        
    }
    return render(request,'index.html',context)    

def inicio(request):
    context={

    }
    return render(request,'index2.html',context)    

def error404(request):
    context={

    }
    return render(request,'error404.html',context)    

def error500(request):
    context={

    }
    return render(request,'error500.html',context)   

def perfil(request):
    context={

    }
    return render(request,'perfil.html',context)   