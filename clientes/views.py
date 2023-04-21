from django.shortcuts import redirect, render
from clientes.forms import ClienteForm, ClienteUpdateForm, CiudadForm

from clientes.models import Cliente
from clientes.models import Ciudad

# Create your views here.


def clientes(request):
    
    clientes= Cliente.objects.all()
    form = ClienteForm(request.POST)
    formCiudad = CiudadForm(request.POST)
    
    context={
        "clientes":clientes,
        'form': form,
        'formCiudad': formCiudad
    }
    return render(request,'clientes/clientes.html',context)

def clientes_ver(request):

    titulo = "Clientes - Ver"
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            return redirect('clientes')
    else:
        form = ClienteForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'clientes/clientes-ver.html', context)



def clientes_crear(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            print('Cliente creado correctamente')

            return redirect('clientes')
        else:
            print('Cliente NO FUÉ CREADO')

        context = {
            'form': form
        }

        return render(request, 'clientes/clientes.html', context)



# def clientes_crear(request):

#     titulo="Clientes - Crear"
#     if request.method=="POST":
#         form= ClienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("El cliente se guardó correctamente")
#             return redirect('clientes')
#         else:
#             print("El cliente NO se guardó")
#     else:
#         form= ClienteForm()
#     context={
#         'titulo':titulo,
#         "form":form
#     }
#     return render(request,'clientes/clientes.html',context)



def clientes_modificar(request,pk, *callback_kwargs):
    titulo = "Clientes - Modificar"
    cliente = Cliente.objects.get(id=pk)
    if request.method == "POST" and 'form-modificar' in request.POST:
        form = ClienteForm(request.POST, instance=Cliente)
        modal_status = 'show'
        pk_cliente = request.POST['pk']
        ## cuerpo del modal ##
        modal_title = f"Modificar {Cliente}"
        modal_submit = "Modificar"
        #######################
        tipo = "modificar"
        form_update = ClienteUpdateForm(instance=Cliente)
        
        cliente = Cliente.objects.get(id=pk_cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')
        else:
            print("Hubo un error al guardar los cambios")
    else:
        form = ClienteForm(instance=Cliente)
    context = {
        'titulo': titulo,
        'form': form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_title,
        'pk': pk_cliente,
        'tipo': tipo,
        'form_update':form_update
    }
    return render(request, 'clientes/clientes-modificar.html', context)



def ciudad_crear(request):
    if request.method == 'POST':
        formCiudad = CiudadForm(request.POST)
        if formCiudad.is_valid():
            formCiudad.save()        
        
            print('Cliente creado correctamente')

            return redirect('clientes')
        else:
            print('Cliente NO FUÉ CREADO')

        context = {
            'form': formCiudad
        }

        return render(request, 'clientes/clientes.html', context)