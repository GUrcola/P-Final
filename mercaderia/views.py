from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render
from mercaderia.models import producto

def crear_producto(request, tipo, modelo):
    
    Producto= producto(tipo= tipo ,modelo= modelo)
    Producto.save()
    
    return render(request, 'mercaderia/crear_producto.html', {"Producto": Producto})


def ver_producto(request):
    
    productos=producto.objects.all()
       
    return render(request, 'mercaderia/ver_producto.html',{"productos": productos})

def Inicio(request):
    
    return render(request, 'mercaderia/inicio.html')

def sobre_mi(request):
    return render(request, 'mercaderia/sobre_mi.html')
