from django.shortcuts import render, redirect
from categoria.models import Categoria
from categoria.forms import CategoriaForm
from django.contrib import messages

# Create your views here.

def categorias(request):

    categorias = Categoria.objects.all()
    form = CategoriaForm()

    for categoria in categorias:
        print(categoria.nombrecat)

    context={

        "categorias": categorias,
        'form': form,
    }
    return render(request,'categoria/categorias.html', context)



def categoria_crear(request):
    titulo = "Categoría - Crear"
    if request.method == 'POST':
        form =  CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Categoría creada correctamente!')
            return redirect(to='categorias')
        else:
            messages.error(request, "¡Error al crear categoría!")
            return redirect(to='categorias')
    else:
        form=CategoriaForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'productos/categoria-crear.html', context)



def categoria_crear_cat(request):

    titulo = "Categoría - Crear"
    if request.method == 'POST':
        form =  CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            print("La categoría se guardó correctamente")
            return redirect('categorias')
        else:
            print("La categoría NO se pudo guardar")
    
    else:
        form = CategoriaForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'productos/categoria-crear.html', context)




def categoria_modificar(request, pk):
    categoria = Categoria.objects.get(id = pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance = categoria)
        if form.is_valid():
            form.save()
            
            return redirect('categorias')
        else:
            print('Error al editar la categoria')
    else:
        form = CategoriaForm(instance = categoria)
    
    context ={
        'form': form,
    }

    return render(request, 'categoria/categorias.html', context)




def categoria_eliminar(request, pk):
    categoria = Categoria.objects.filter(id = pk).update(
        estadocat = '0'
    )
    messages.success(request, "Categoría eliminada satisfactoriamente!")
    return redirect('categorias') 



#Function to RECUPERAR categorias
def recuperar_categoria(request):
    
    categorias= Categoria.objects.all()
    categorias_recuperables = []

    for categoria in categorias:
        if categoria.estadocat != '1':
            categorias_recuperables.append(categoria)

    context={
        "categorias":categorias_recuperables
    }
    return render(request,'categoria/categorias-recuperar.html',context)



def recuperar_cat(request, pk):
    titulo = 'Recuperar Categoría'
    Categoria.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "Categoría restaurada satisfactoriamente!")
    return redirect('categorias')
