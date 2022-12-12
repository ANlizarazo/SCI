from django.shortcuts import render

# Create your views here.
def compras(request):
    context={

    }
    return render(request,'compras/compras.html',context)