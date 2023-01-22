from pyexpat.errors import messages
from django.shortcuts import render, redirect
from usuarios.forms import UsuarioForm, UsuarioUpdateForm

from usuarios.models import Usuario

# Create your views here.
def usuarios(request):

    usuarios= Usuario.objects.all()

    context={
        "usuarios": usuarios
    }
    return render(request,'usuarios/usuarios.html',context)

def usuarios_ver(request):

    titulo = "Usuarios - Ver"
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'usuarios/usuarios-ver.html', context)

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

def usuarios_modificar(request,pk, *callback_kwargs):
    titulo = "Usuarios - Modificar"
    Usuario = Usuario.objects.get(id=pk)
    if request.method == "POST" and 'form-modificar' in request.POST:
        form = UsuarioForm(request.POST, instance=Usuario)
        modal_status = 'show'
        pk_usuario = request.POST['pk']
        ## cuerpo del modal ##
        modal_title = f"Modificar {Usuario}"
        modal_submit = "Modificar"
        #######################
        tipo = "modificar"
        form_update = UsuarioUpdateForm(instance=Venta)
        
        Venta = Venta.objects.get(id=pk_usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print("Hubo un error al guardar los cambios")
    else:
        form = UsuarioForm(instance=Venta)
    context = {
        'titulo': titulo,
        'form': form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_title,
        'pk': pk_usuario,
        'tipo': tipo,
        'form_update':form_update
    }
    return render(request, 'usuarios/usuarios-modificar.html', context)


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
