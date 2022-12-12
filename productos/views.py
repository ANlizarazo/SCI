from django.shortcuts import render

# Create your views here.
def productos(request):
    context={

    }
    return render(request,'productos/productos.html',context)