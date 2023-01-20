from django.shortcuts import redirect, render
from tecnicos.forms import TecnicoForm

from tecnicos.models import Tecnico

# Create your views here.


def tecnicos(request):
    
    tecnicos= Tecnico.objects.all()
    
    context={
        "tecnicos":tecnicos
    }
    return render(request,'tecnicos/tecnicos.html',context)

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
    return render(request,'tecnicos/tecnicos-crear.html',context)