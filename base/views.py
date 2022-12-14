from django.shortcuts import render, redirect as shortcuts

def login(request):
    context={
        
    }
    return render(request,'index.html',context)    

def inicio(request):
    context={

    }
    return render(request,'index2.html',context)    