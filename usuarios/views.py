from django.shortcuts import redirect, render
from usuarios.models import Usuario
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# se incluyen las siguientes importaciones
from django.contrib.auth.models import User
from usuarios.forms import UsuarioForm

# List to Usuario
def usuarios (request):
    
    #importar los usuarios desde el modulo admin
    usuarios=Usuario.objects.all()
    form = UsuarioForm()

    context = {
        'usuarios': usuarios,
        'form': form,
    }

    return render(request,'usuarios/usuarios.html', context)

#Function to ADD usuario
def usuario_crear(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.create_user(request.POST['email'], request.POST['email'], '123')
            user.save()
            messages.success(request,'¡Usuario creado correctamente!')
            return redirect('usuarios')
        else:
            messages.error(request, "¡Error al crear usuario!")
            return redirect('usuarios')
    else:
        form = UsuarioForm()

    context={
        'form': form,
    }

    return render(request, 'usuarios/usuarios-crear.html', context)
        
#Function to View  usuario data individually
def usuario_ver(request, pk):
    usuario = Usuario.objects.get(id = pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            messages.error(request,'¡Error al ver usuario!')
            print("Error al editar usuario")
    else: 
        form = UsuarioForm(instance = usuario)

    return render(request)

#Function to EDIT usuario
"""def usuario_modificar(request):
    if request.method == "POST":
        usuario = Usuario.objects.get(id = request.POST.get('id'))
        if usuario != None: 
            usuario.foto= request.POST.get('foto')
            usuario.nombres= request.POST.get('nombres')
            usuario.apellidos= request.POST.get('apellidos')
            usuario.telefono= request.POST.get('telefono')
            usuario.email= request.POST.get('email')
            usuario.direccion= request.POST.get('direccion')
            usuario.tipoDocumento= request.POST.get('tipoDocumento')
            usuario.numDocumento= request.POST.get('numDocumento')
            usuario.genero= request.POST.get('genero')
            usuario.estado= request.POST.get('estado')
            usuario.save()
            messages.success(request, "Usuario Actualizado con éxito!")
            return HttpResponseRedirect("usuarios/")"""

def usuario_modificar(request, pk):
    usuario = Usuario.objects.get(id = pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Usuario modificado correctamente!')
            return redirect('usuarios')
        else:
            messages.error(request, "¡Error al modificar usuario!")
            return redirect('usuarios')
    else:
        form = UsuarioForm(instance = usuario)

    return render(request, 'usuarios/usuarios.html', {'form': form})


#Function to DELETE usuario
"""def delete_usuario(request, usuario_id):
    if request.method == "POST":
        usuario = Usuario.objects.get(id= usuario_id)
        usuario.delete()
        messages.success(request, "Usuario eliminado satisfactoriamente!")
        return redirect("usuarios")
"""
def usuarios_eliminar(request, pk):
    usuario = Usuario.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "Usuario eliminado satisfactoriamente!")
    return redirect('usuarios') 

#Function to RECUPERAR usuarios
def recuperar_usuarios(request):
    
    usuarios= Usuario.objects.all()
    usuarios_recuperables = []

    for usuario in usuarios:
        if usuario.estado == '0':
            usuarios_recuperables.append(usuario)

    context={
        "usuarios":usuarios_recuperables
    }
    return render(request,'usuarios/usuarios-recuperar.html',context)

def recuperar(request, pk):
    titulo = 'Recuperar Usuario'
    Usuario.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "Usuario restaurado satisfactoriamente!")
    return redirect('usuarios')

################################ EJEMPLO ####################################

""""
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