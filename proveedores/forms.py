from django import forms    

class ProveedorFormulario(forms.Form):
        razon_social=forms.CharField( max_length=20)
        ubicacion=forms.CharField(max_length=50)
        
        
class BuscadorP(forms.Form):
        razon_social=forms.CharField( max_length=20)   
                