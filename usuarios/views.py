from django.shortcuts import redirect, render
from usuarios.models import Usuario
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views.generic import CreateView
from .forms import FormUsuario

# Create your views here.

def usuarios (request):
    
    #importar los usuarios desde el modulo admin
    usuarios_list=Usuario.objects.all()

    return render(request,'usuarios/usuarios.html',  {"usuarios": usuarios_list})

#Function to ADD usuario
class CrearUsuario(CreateView):
    model = Usuario
    form_class = FormUsuario
    template_name = ('usuarios/usuarios.html')
    success_url = reverse_lazy('usuario')

#Function to View  usuario data individually
def usuario_ver(request, usuario_id):
    usuario = Usuario.objects.get( id = usuario_id) 
    if usuario != None:
        return render(request, "usuarios/usuarios-modificar.html", {'usuario':usuario} )
    else:
        return redirect('usuarios/usuarios-ver.html')

#Function to EDIT usuario
def usuario_modificar(request):
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
            return HttpResponseRedirect("usuarios/")

#Function to DELETE usuario
def delete_usuario(request, usuario_id):
    if request.method == "POST":
        usuario = Usuario.objects.get(id= usuario_id)
        usuario.delete()
        messages.success(request, "Usuario eliminado satisfactoriamente!")
        return redirect("usuarios")




################################ EJEMPLO DE USUARIO ####################################

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
