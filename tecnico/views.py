from django.shortcuts import redirect, render
from tecnico.forms import TecnicoForm

from tecnico.models import Tecnico

# Create your views here.


def tecnicos(request):
    
    tecnicos= Tecnico.objects.all()
    
    context={
        "tecnicos":tecnicos
    }
    return render(request,'tecnico/tecnico.html',context)

def tecnicos_crear(request):

    titulo="Tecnicos - Crear"
    if request.method == "POST":
        form=TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            print("El técnico se guardó correctamente")
            return redirect('tecnicos')
        else:
            print("El técnico NO se guardó correctamente")
    else:
        form=TecnicoForm()
    context={
            'titulo':titulo,
            "form":form
    }
    return render(request,'tecnico/tecnicos-crear.html',context)