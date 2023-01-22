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