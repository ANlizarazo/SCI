from pyexpat.errors import messages
from django.shortcuts import redirect, render
from tecnico.forms import TecnicoForm, TecnicoUpdateForm
from tecnico.models import Tecnico

# Create your views here.


def tecnicos(request):
    
    tecnicos= Tecnico.objects.all()
    
    context={
        "tecnicos":tecnicos
    }
    return render(request,'tecnico/tecnico.html',context)

    
def tecnicos_ver(request):

    titulo = "Técnicos - Ver"
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
    return render(request, 'tecnico/tecnico-ver.html', context)


def tecnicos_crear(request):

    titulo = "Tecnicos - Crear"
    if request.method == 'POST' and 'form-crear' in request.POST:
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            print("El tecnico se guardó correctamente")
            return redirect('ventas')
        else:
            print("El tecnico NO se pudo guardar")
    else:
        form = TecnicoForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'tecnico/tecnico-crear.html', context)


def tecnicos_modificar(request,pk, *callback_kwargs):
    titulo = "tecnicos - Modificar"
    Tecnico = tecnicos.objects.get(id=pk)
    if request.method == "POST" and 'form-modificar' in request.POST:
        form = TecnicoForm(request.POST, instance=Tecnico)
        modal_status = 'show'
        pk_tecnico = request.POST['pk']
        ## cuerpo del modal ##
        modal_title = f"Modificar {Tecnico}"
        modal_submit = "Modificar"
        #######################
        tipo = "modificar"
        form_update = TecnicoUpdateForm(instance=Tecnico)
        
        Tecnico = Tecnico.objects.get(id=pk_tecnico)
        if form.is_valid():
            form.save()
            return redirect('tecnicos')
        else:
            print("Hubo un error al guardar los cambios")
    else:
        form = TecnicoForm(instance=Tecnico)
    context = {
        'titulo': titulo,
        'form': form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_title,
        'pk': pk_tecnico,
        'tipo': tipo,
        'form_update':form_update
    }
    return render(request, 'tecnico/tecnico-modificar.html', context)

    from django.shortcuts import redirect, render
from tecnico.models import Tecnico
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def tecnicos (request):
    
    #importar los tecnicos desde el modulo admin
    tecnicos_list= Tecnico.objects.all()

    return render(request,'tecnico/tecnico.html',  {"tecnico": tecnicos_list})

#Function to ADD tecnico
def tecnico_crear(request):
    if request.method=="POST":
        if request.POST.get('nombres') \
            and request.POST.get('apellidos') \
            and request.POST.get('telefono') \
            and request.POST.get('genero') \
            and request.POST.get('tipoDocumento') \
            and request.POST.get('numDocumento') \
            and request.POST.get('estado') \
            and request.POST.get('ciudad'):
            tecnico= Tecnico()  
            tecnico.nombres= request.POST.get('nombres')
            tecnico.apellidos= request.POST.get('apellidos')
            tecnico.telefono= request.POST.get('telefono')
            tecnico.genero= request.POST.get('genero')
            tecnico.tipoDocumento= request.POST.get('tipoDocumento')
            tecnico.numDocumento= request.POST.get('numDocumento')
            tecnico.estado= request.POST.get('estado')
            tecnico.estado= request.POST.get('ciudad')
            tecnico.save()
            messages.success(request, "Tecnico añadido con éxito!")
            return redirect('tecnico')
        else:
            messages.error(request, "La creación del tecnico ha fallido!")
            return redirect('tecnico')

#Function to View tecnico data individually
def tecnico_ver(request, tecnico_id):
    tecnico = Tecnico.objects.get( id = tecnico_id) 
    if tecnico != None:
        return render(request, "tecnico/tecnico-modificar.html", {'tecnico':tecnico} )
    else:
        return redirect('tecnico/tecnico-ver.html')

#Function to EDIT tecnico
def tecnico_modificar(request):
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
            return HttpResponseRedirect("tecnico/")

#Function to DELETE tecnico
def delete_tecnico(request, tecnico_id):
    if request.method == "POST":
        tecnico = Tecnico.objects.get(id= tecnico_id)
        tecnico.delete()
        messages.success(request, "Técnico eliminado satisfactoriamente!")
        return redirect("tecnico")


