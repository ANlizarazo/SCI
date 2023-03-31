from django.shortcuts import redirect, render
from tecnico.models import Tecnico
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def tecnicos (request):
    
    #importar los tecnicos desde el modulo admin
    tecnicos_list= Tecnico.objects.all()

    return render(request,'tecnico/tecnico.html',  {"tecnico": tecnicos_list})

#Function to ADD tecnico
def tecnico_crear(request):
    if request.method=="POST":
        if request.POST.get('nombres') \
            and request.POST.get('apellidos') \
            and request.POST.get('telefono') \
            and request.POST.get('genero') \
            and request.POST.get('tipoDocumento') \
            and request.POST.get('numDocumento') \
            and request.POST.get('estado') \
            and request.POST.get('ciudad'):
            tecnico= Tecnico()  
            tecnico.nombres= request.POST.get('nombres')
            tecnico.apellidos= request.POST.get('apellidos')
            tecnico.telefono= request.POST.get('telefono')
            tecnico.genero= request.POST.get('genero')
            tecnico.tipoDocumento= request.POST.get('tipoDocumento')
            tecnico.numDocumento= request.POST.get('numDocumento')
            tecnico.estado= request.POST.get('estado')
            tecnico.estado= request.POST.get('ciudad')
            tecnico.save()
            messages.success(request, "Tecnico añadido con éxito!")
            return redirect('tecnicos')
        else:
            messages.error(request, "La creación del tecnico ha fallido!")
            return redirect('tecnico')

#Function to View tecnico data individually
def tecnico_ver(request, tecnico_id):
    tecnico = Tecnico.objects.get( id = tecnico_id) 
    if tecnico != None:
        return render(request, "tecnico/tecnico-modificar.html", {'tecnico':tecnico})
    else:
        return redirect('tecnico/tecnico-ver.html')

#Function to EDIT tecnico
def tecnico_modificar(request):
    if request.method == "POST":
        tecnico = Tecnico.objects.get(id = request.POST.get('id'))
        if tecnico != None: 
            tecnico.nombres= request.POST.get('nombres')
            tecnico.apellidos= request.POST.get('apellidos')
            tecnico.telefono= request.POST.get('telefono')
            tecnico.genero= request.POST.get('genero')
            tecnico.tipoDocumento= request.POST.get('tipoDocumento')
            tecnico.numDocumento= request.POST.get('numDocumento')
            tecnico.estado= request.POST.get('estado')
            tecnico.estado= request.POST.get('ciudad')
            tecnico.save()
            messages.success(request, "Técnico Actualizado con éxito!")
            return HttpResponseRedirect("tecnico/")

#Function to DELETE tecnico
"""def delete_tecnico(request, tecnico_id):
    if request.method == "POST":
        tecnico = Tecnico.objects.get(id= tecnico_id)
        tecnico.delete()
        messages.success(request, "Técnico eliminado satisfactoriamente!")
        return redirect("tecnico")
"""
def tecnicos_eliminar(request, pk):
    tecnico = Tecnico.objects.filter(id = pk).update(
        estado = '0'
    )
    messages.success(request, "Técnico eliminado satisfactoriamente!")
    return redirect('tecnico') 

#Function to RECUPERAR tecnicos
def recuperar_tecnicos(request):
    
    tecnicos= Tecnico.objects.all()
    tecnicos_recuperables = []

    for tecnico in tecnicos:
        if tecnico.estado == '0':
            tecnicos_recuperables.append(tecnico)

    context={
        "tecnico":tecnicos_recuperables
    }
    return render(request,'tecnico/tecnico-recuperar.html',context)

def recuperar(request, pk):
    titulo = 'Recuperar Tecnico'
    Tecnico.objects.filter(id = pk).update(
        estado = '1'
    )
    messages.success(request, "Técnico restaurado satisfactoriamente!")
    return redirect('tecnico')