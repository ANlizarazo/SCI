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