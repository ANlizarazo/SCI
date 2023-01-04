from django.shortcuts import render

# Create your views here.
def ventas(request):
    context={

    }
    return render(request,'ventas/ventas.html',context)

def ventas_crear(request):
    