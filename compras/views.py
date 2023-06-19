from django.shortcuts import redirect, render
import compras
from compras.forms import CompraForm,CompraUpdateForm
from django.contrib import messages
from compras.models import Compra

# se incluyen las siguientes importaciones
from django.contrib.auth.models import User


# Create your views here.

def compras (request):
    
    #importar los compras desde el modulo admin
    compras_list=Compra.objects.all()

    return render(request,'compras/compras.html',  {"compras": compras_list})

#Function to ADD compra
def compras_crear(request):
    if request.method == 'POST':
        form =CompraForm(request.POST)
        if form.is_valid():
            form.save()
            compra = Compra(request.POST['email'], request.POST['email'], '123')
            compra.save()
            messages.success(request,"Compra creado satisfastoriamente!")
            return redirect('compras')
        else:
            print('Error al crear la compra')
    else:
        form = CompraForm()

    return render(request, 'compras/compras.html', {'form': form})
        



#Function to View  compra data individually

    
def compras_ver(request, pk):
    compra = Compra.objects.get(id = pk)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance =compra)
        if form.is_valid():
            form.save()
            messages.success(request, "compra modificado")
            return redirect('compras')
        else:
            print("Error al editar la compra")
    else: 
        form = CompraForm(instance = compra)

    return render(request)

#Function to EDIT compra

def compras_modificar(request, pk):
    compra = Compra.objects.get(id = pk)
    if request.method == "POST":
        form = CompraForm(request.POST, instance = compras)
        if form.is_valid():
            form.save()
            messages.success(request, "Compra Actualizado con éxito!")
            return redirect('Compras')
        else:
            messages.error(request, "Compra No Actualizado, hubo un error!")
            return redirect('Compras')
    else:
        form = CompraForm(instance = compras)

    return render(request, 'compras/compras.html', {'form': form})


#Function to DELETE compra

def compras_eliminar(request, pk):
    compra = Compra.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "Compra eliminado satisfactoriamente!")
    return redirect('compras') 

#Function to RECUPERAR compras
def recuperar_compras(request):
    
    compras= Compra.objects.all()
    compras_recuperables = []

    for compra in compras:
        if compra.estado == '0':
            compras_recuperables.append(compra)

    context={
        "compras":compras_recuperables
    }
    return render(request,'compras/compras-recuperar.html',context)

def recuperar(request, pk):
    titulo = 'Recuperar Compra'
    Compra.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "Compra restaurado satisfactoriamente!")
    return redirect('compras')


