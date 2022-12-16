from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from mercaderia.models import producto
from mercaderia.forms import FormularioProd, FormularioBusqueda
from django.views.generic import View
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView

def crear_producto(request):
    
    if request.method == 'POST':
        formulario = FormularioProd(request.POST)
        if formulario.is_valid():   
            tipo=request.POST['tipo']
            modelo=request.POST ['modelo']
            descripcion=request.POST ['descripcion']
            Producto= producto(tipo= tipo ,modelo= modelo, descripcion= descripcion)
            Producto.save()
            return redirect ('ver_productos')
    
    formulario=FormularioProd()
    
    return render(request, 'mercaderia/crear_producto.html', {'formulario':formulario})


def ver_producto(request):
    
    tipo=request.GET.get('tipo', None)
    
    if tipo:
        productos = producto.objects.filter(tipo__icontains=tipo)
    else:
        productos=producto.objects.all()
    
    formulario= FormularioBusqueda()
       
    return render(request, 'mercaderia/ver_producto.html',{"productos": productos, 'formulario':formulario})

def Inicio(request):
    
    return render(request, 'mercaderia/inicio.html')

def sobre_mi(request):
    return render(request, 'mercaderia/sobre_mi.html')


def eliminarM(request, id):
    mercaderia= producto.objects.get(id=id)
    mercaderia.delete()
    return redirect('ver_productos')

class ver_prod(DetailView):
    model= producto
    template_name= 'mercaderia/ver_prod.html'
    
    
class editar_prod(LoginRequiredMixin, UpdateView):
    model = producto
    success_url = '/ver_producto/'
    template_name = 'mercaderia/editar_producto.html'
    fields = ['tipo', 'modelo', 'descripcion']