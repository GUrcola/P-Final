from django import forms
class FormularioProd(forms.Form):
    tipo=forms.CharField(max_length=30)
    modelo=forms.IntegerField()
    
class FormularioBusqueda(forms.Form):
    tipo=forms.CharField(max_length=30, required=False)   