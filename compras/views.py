from django.shortcuts import render, redirect

from compras.models import Compra

# Create your views here.
def compras(request):

    compras= Compra.objects.all()

    context={
        "compras":compras
    }
    return render(request,'compras/compras.html',context)
