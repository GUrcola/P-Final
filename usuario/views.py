from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login as Inicio_Sesion
from django.contrib.auth.mixins import LoginRequiredMixin
from usuario.forms import EditarPerfil, EditarContraseña
from django.contrib.auth.views import PasswordChangeView
from usuario.models import UsuarioExt
def login(request):
    
    if request.method == 'POST':
        formulario=AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.get_user() 
            Inicio_Sesion(request, usuario)
            extencion, nuevo=UsuarioExt.objects.get_or_create(user=request.user)  
            return redirect ('Inicio') 
    else:
        formulario=AuthenticationForm()
            
    
    return render (request, 'usuario/login.html',{'formulario':formulario})


def crear(request):
    if request.method == 'POST':
        
        formulario=UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect ('Inicio')   
    else:    
        formulario=UserCreationForm()
    return render(request, 'usuario/crear.html', {'formulario':formulario})

def perfil(request):
    
    extencion, nuevo=UsuarioExt.objects.get_or_create(user=request.user) 
    
    return render(request, 'usuario/perfil.html', {})


def editar_perfil(request):
    
    user= request.user
    user.usuarioext
        
    if request.method == 'POST':
        formulario=EditarPerfil(request.POST)
        if formulario.is_valid():
            data_nueva= formulario.cleaned_data
            request.user.first_name=data_nueva['first_name']
            request.user.last_name=data_nueva['last_name']
            request.user.email=data_nueva['email']
            request.user.pais=data_nueva['pais']
            request.user.save()
            return redirect('perfil')
    else: 
        formulario=EditarPerfil(initial={'first_name':request.user.first_name, 'last_name':request.user.last_name, 'email':request.user.email})
    return render(request, 'usuario/edit_p.html', {'formulario':formulario})


class CambiarMiContraseña(LoginRequiredMixin,PasswordChangeView):
    template_name='usuario/edit_c.html'
    success_url= '/usuario/perfil'
    
