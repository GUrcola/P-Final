from django import forms

class EditarPerfil(forms.Form):
    email= forms.CharField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    