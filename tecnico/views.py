from django.shortcuts import redirect, render
from tecnico.models import Tecnico
from tecnico.forms import TecnicoForm
from django.contrib import messages

# Create your views here.

def tecnicos (request):

    tecnico_list= Tecnico.objects.all()
    form = TecnicoForm()

    context= {
        'tecnico_list': tecnico_list,
        'form': form,
    }
    return render(request,'tecnico/tecnico.html', context)

#Function to ADD tecnico
def tecnico_crear(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'¡Técnico creado correctamente!')
            return redirect('tecnico')
        else:
            messages.error(request, "¡Error al crear técnico!")
            return redirect('tecnico')
    else:
        form = TecnicoForm()
    context = {
        'form': form,
    }

    return render(request, 'tecnico/tecnico-crear.html', context)

#Function to View tecnico data individually
def tecnico_ver(request):

    titulo = "Técnico - Ver"
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            return redirect('tecnicos')
    else:
        form = TecnicoForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'tecnico/tecnico.html', context)



#Function to modificar tecnico
def tecnico_modificar(request, pk):
    tecnico = Tecnico.objects.get(id = pk)
    if request.method == "POST":
        form = TecnicoForm(request.POST, instance = tecnico)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Técnico modificado correctamente!")
            return redirect('tecnico')
        else:
            messages.error(request, "¡Error al modificar técnico!")
            return redirect('tecnico')
    else:
        form = TecnicoForm(instance = tecnico)
    
    context ={
        'form': form,
    }

    return render(request, 'tecnico/tecnico.html', context)

"""def tecnico_modificar(request):
    if request.method == "POST":
        tecnico = Tecnico.objects.get(id = request.POST.get('id'))
        if tecnico != None: 
            tecnico.nombres= request.POST.get('nombres')
            tecnico.apellidos= request.POST.get('apellidos')
            tecnico.telefono= request.POST.get('telefono')
            tecnico.genero= request.POST.get('genero')
            tecnico.tipoDocumento= request.POST.get('tipoDocumento')
            tecnico.numDocumento= request.POST.get('numDocumento')
            tecnico.estado= request.POST.get('estado')
            tecnico.estado= request.POST.get('ciudad')
            tecnico.save()
            messages.success(request, "Técnico Actualizado con éxito!")
            return HttpResponseRedirect("tecnico/")"""

#Function to DELETE tecnico
"""def delete_tecnico(request, tecnico_id):
    if request.method == "POST":
        tecnico = Tecnico.objects.get(id= tecnico_id)
        tecnico.delete()
        messages.success(request, "Técnico eliminado satisfactoriamente!")
        return redirect("tecnico")
"""
def tecnicos_eliminar(request, pk):
    tecnico = Tecnico.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "Técnico eliminado satisfactoriamente!")
    return redirect('tecnico') 

#Function to RECUPERAR tecnicos
def recuperar_tecnicos(request):
    
    tecnicos= Tecnico.objects.all()
    tecnicos_recuperables = []

    for tecnico in tecnicos:
        if tecnico.estado == '0':
            tecnicos_recuperables.append(tecnico)

    context={
        "tecnico":tecnicos_recuperables
    }
    return render(request,'tecnico/tecnico-recuperar.html',context)

def recuperar_tecnico(request, pk):
    titulo = 'Recuperar Tecnico'
    Tecnico.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "Técnico restaurado satisfactoriamente!")
    return redirect('tecnico')