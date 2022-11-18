from django import forms
class FormularioProd(forms.Form):
    tipo=forms.CharField(max_length=30)
    modelo=forms.IntegerField()
    descripcion=forms.CharField(max_length=50)
    
class FormularioBusqueda(forms.Form):
    tipo=forms.CharField(max_length=30, required=False)   