from django.shortcuts import render, redirect
import sys
from django.core.management import call_command
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def basedatos(request):
    titulo = 'Base Datos'
    context = {
        'titulo': titulo
    }
    
    return render(request, 'basedatos/basedatos.html', context)


def respaldar_base_datos(request):
    sysout = sys.stdout
    sys.stdout = open('db.json','w',1,'utf-8')    
    call_command('dumpdata')   
    sys.stdout = sysout    
    messages.success(request, 'Se respaldó la base de datos')   
    
    return redirect('basedatos')
  


def recuperar_base_datos(request):
    call_command('loaddata', 'db.json')
    messages.success(request, 'Se recuperó la base de datos')
    return redirect('basedatos')
    