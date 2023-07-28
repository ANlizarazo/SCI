from django.shortcuts import redirect, render
from usuarios.models import Usuario
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# se incluyen las siguientes importaciones
from django.contrib.auth.models import User
from usuarios.forms import UsuarioForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('usuarios.view_usuario')
# List to Usuario
def usuarios (request):
    #importar los usuarios desde el modulo admin
    usuarios=Usuario.objects.all()
    form = UsuarioForm()

    for usuario in usuarios:
        print(usuario.nombres)

    context = {
        'usuarios': usuarios,
        'form': form,
    }

    return render(request,'usuarios/usuarios.html', context)

#Function to ADD usuario
def usuario_crear(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            if not User.objects.filter(username=request.POST['numDocumento']):
                user = User.objects.create_user('nombre','email@email','pass')
                user.username = request.POST['numDocumento']
                user.first_name= request.POST['nombres']
                user.last_name= request.POST['apellidos']
                user.email= request.POST['email']
                user.password=make_password("@"+request.POST['numDocumento'])
                user.save()
                """user_group= User
                my_group = Group.objects.get(name= 'usuario.rol')
                usuario.user.groups.clear()
                my_group.user_set.add(usuario.user)"""
            else:
                user= User.objects.get(username=request.POST['numDocumento'])
            
            usuario = Usuario.objects.create(
                nombres= request.POST['nombres'],
                apellidos= request.POST['apellidos'],
                telefono= request.POST['telefono'],
                email= request.POST['email'],
                direccion= request.POST['direccion'],
                tipoDocumento= request.POST['tipoDocumento'],
                numDocumento= request.POST['numDocumento'],
                genero= request.POST['genero'],
                rol= request.POST['rol'],
                foto = form.cleaned_data.get('foto'),
                user= user
            )
            return redirect('usuarios')
        else:
            form = UsuarioForm(request.POST,request.FILES)
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

    context={
        'form':form
    }

    return render(request, 'usuarios/usuarios.html', context)


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

