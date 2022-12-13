from django.shortcuts import render

# Create your views here.
def ventas(request):
    context={

    }
    return render(request,'base/templates/ventas/ventas.html',context)