from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from mercaderia.models import producto
from mercaderia.forms import FormularioProd

def crear_producto(request):
    
    if request.method == 'POST':
        formulario = FormularioProd(request.POST)
        if formulario.is_valid():   
            tipo=request.POST['tipo']
            modelo=request.POST ['modelo']
            Producto= producto(tipo= tipo ,modelo= modelo)
            Producto.save()
            return redirect ('ver_productos')
    
    formulario=FormularioProd()
    
    return render(request, 'mercaderia/crear_producto.html', {'formulario':formulario})


def ver_producto(request):
    
    productos=producto.objects.all()
       
    return render(request, 'mercaderia/ver_producto.html',{"productos": productos})

def Inicio(request):
    
    return render(request, 'mercaderia/inicio.html')

def sobre_mi(request):
    return render(request, 'mercaderia/sobre_mi.html')
