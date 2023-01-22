from django.shortcuts import redirect, render
from compras.forms import CompraForm,CompraUpdateForm
from compras.models import Compra

# Create your views here.
def compras(request):

    compras= Compra.objects.all()

    context={
        "compras":compras
    }
    return render(request,'compras/compras.html',context)

def compras_ver(request):

    titulo = "Compras - Ver"
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            return redirect('compras')
    else:
        form = CompraForm()
    context = {
        'titulo': titulo,
        "form": form
    }
    return render(request, 'compras/compras-ver.html', context)

def compras_crear(request):

    titulo="Compras - Crear"
    if request.method == 'POST'and 'form-crear' in request.POST:    
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
    return render(request,'compras/compras-crear.html',context)

def compras_modificar(request,pk, *callback_kwargs):
    titulo = "Compras - Modificar"
    compra = Compra.objects.get(id=pk)
    if request.method == "POST" and 'form-modificar' in request.POST:
        form = CompraForm(request.POST, instance=Compra)
        modal_status = 'show'
        pk_compra = request.POST['pk']
        ## cuerpo del modal ##
        modal_title = f"Modificar {Compra}"
        modal_submit = "Modificar"
        #######################
        tipo = "modificar"
        form_update = CompraUpdateForm(instance=Compra)
        
        compra = Compra.objects.get(id=pk_compra)
        if form.is_valid():
            form.save()
            return redirect('compras')
        else:
            print("Hubo un error al guardar los cambios")
    else:
        form = CompraForm(instance=Compra)
    context = {
        'titulo': titulo,
        'form': form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_title,
        'pk': pk_compra,
        'tipo': tipo,
        'form_update':form_update
    }
    return render(request, 'compras/compras-modificar.html', context)