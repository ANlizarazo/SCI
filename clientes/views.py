from django.shortcuts import render

# Create your views here.
def clientes(request):
    
    context={

    }
    return render(request,'clientes/clientes.html',context)