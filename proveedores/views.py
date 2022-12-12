from django.shortcuts import render

# Create your views here.
def proveedores(request):
    context={

    }
    return render(request,'proveedores/proveedores.html',context)