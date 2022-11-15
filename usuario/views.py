from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as Inicio_Sesion
def login(request):
    
    if request.method == 'POST':
        formulario=AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.get_user()
            Inicio_Sesion(request, usuario)  
            return redirect ('Inicio') 
    else:
        formulario=AuthenticationForm()
            
    
    return render (request, 'usuario/login.html',{'formulario':formulario})


