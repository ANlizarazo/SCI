from django.shortcuts import render, redirect
from usuarios.forms import UsuarioForm

from usuarios.models import Usuario

# Create your views here.
def usuarios(request):

    usuarios= Usuario.objects.all()

    context={
        "usuarios": usuarios
    }
    return render(request,'usuarios/usuarios.html',context)

def usuarios_crear(request):

    titulo="Usuarios - Crear"
    if request.method == "POST":
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            print("El usuario se guardó correctamente")
            return redirect('usuarios')
        else:
            print("El usuario NO se guardó correctamente")
    else:
        form=UsuarioForm()
    context={
            'titulo':titulo,
            "form":form
    }
    return render(request,'usuarios/usuarios-crear.html',context)

"""
def usuarios_crear(request):
    titulo="Usuarios - Crear"
    if request.method == "POST":
        form= UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            if not Usuario.objects.filter(username=request.POST['documento']):
                user = Usuario.objects.create_user('nombre','email@email','pass')
                user.username= request.POST['documento']
                user.first_name= request.POST['nombres']
                user.last_name= request.POST['apellidos']
                user.email= request.POST['email']
                user.password=make_password("@" + request.POST['nombres'][0] + request.POST['apellidos'][0] + request.POST['documento'][-4:])
                user.save()
                user_group = User
                my_group= Group.objects.get(name='Normal')
                usuario.user.groups.clear()
                my_group.user_set.add(usuario.user)
            else:
                user=User.objects.get(username=request.POST['documento'])

            usuario= Usuario.objects.create(
                nombres=request.POST['nombres'],
                apellidos=request.POST['apellidos'],
                foto=form.cleaned_data.get('foto'),
                email=request.POST['email'],
                tipoDocumento=request.POST['tipoDocumento'],
                documento=request.POST['documento'],
                telefono=request.POST['telefono'],
                direccion=request.POST['direccion'],
                municipio=Municipio.objects.get(id=int(request.POST['municipio'])),
                fecha_nacimiento=request.POST['fecha_nacimiento'],
                empresa=Empresa.objects.get(id=int(request.POST['empresa'])),
                user=user,
                rol=request.POST['rol'],
            )
            return redirect('usuarios')
        else:
            form = UsuarioForm(request.POST,request.FILES)
    else:
        form= UsuarioForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'usuarios/usuarios-crear.html',context)
"""
