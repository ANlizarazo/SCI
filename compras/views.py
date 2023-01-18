from django.shortcuts import redirect, render
from compras.forms import CompraForm
from compras.models import Compra

# Create your views here.
def compras(request):

    compras= Compra.objects.all()

    context={
        "compras":compras
    }
    return render(request,'compras/compras.html',context)

def compras_crear(request):

    titulo="Compras - Crear"
    if request.method == 'POST':    
        form= CompraForm(request.POST)
        if form.is_valid():
            form.save()
            print("La compra se guardó correctamente")
        else:
            print("La compre no se guardó")
    else:
        form= CompraForm()

    context={
        'titulo':titulo,
        "form":form
    }
    return render(request,'compras/compras_crear.html',context)