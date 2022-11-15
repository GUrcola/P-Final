from django.shortcuts import render
from proveedores.models import proveedores
from proveedores.forms import ProveedorFormulario, BuscadorP
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
def nuevo_proveedor(request):
    if request.method == 'POST':
        formulario = ProveedorFormulario(request.POST)
        if formulario.is_valid():   
            razon_social=request.POST['razon_social']
            ubicacion=request.POST ['ubicacion']
            Proveedor= proveedores(razon_social= razon_social ,ubicacion= ubicacion)
            Proveedor.save()
            return redirect ('ver_proveedor')
    
    formulario=ProveedorFormulario()
    
    
    return render(request,'proveedores/nuevo_proveedor.html',{'formulario':formulario} )  

def ver_proveedor(request):
    
    Mis_Proveedores=proveedores.objects.all()
    return render (request,'proveedores/ver_proveedores.html',{'Mis_Proveedores':Mis_Proveedores} )

def eliminar(request, id):
    proveedor= proveedores.objects.get(id=id)
    proveedor.delete()
    return redirect('ver_proveedor')

class editar(UpdateView):
    model= proveedores
    success_url= 'proveedores/ver/'
    fields=['razon_social', 'ubicacion']
    template_name= 'proveedores/editar.html'
    
    
    
# def editar(request, id):
    
#     proveedor=proveedores.objects.get(id=id)
   
#     if request.method == 'POST':
#         formulario = ProveedorFormulario(request.POST)
#         if formulario.is_valid():
#             datos=formulario.cleaned_data
            
#             proveedor.razon_social=datos('razon_social')
#             proveedor.ubicacion=datos('ubicacion')
#             proveedor.save()
            
#             return redirect ('ver_proveedor')
    
   
#     formulario=ProveedorFormulario(initial={'razon_social':proveedor.razon_social, 'ubicacion':proveedor.ubicacion})
    
#     return render(request,'proveedores/editar.html',{'formulario':formulario},{'proveedor':proveedor} )