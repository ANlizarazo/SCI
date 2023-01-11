from django.shortcuts import render, redirect

from usuarios.models import Usuario

# Create your views here.
def usuarios(request):

    usuarios= Usuario.objects.all()

    context={
        "usuarios": usuarios
    }
    return render(request,'usuarios/usuarios.html',context)
