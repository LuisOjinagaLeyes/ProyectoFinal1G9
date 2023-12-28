from django import forms
from .models import Noticia
from django.forms import TextInput, Textarea

class Formulario_Noticia(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields =['titulo','contenido','imagen','categoria']

class Formulario_Modificar_Noticia(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields =['titulo','contenido','imagen','categoria']
        widgets = {
            'titulo': TextInput(attrs={
                'placeholder': 'Ingrese el titulo',
                'class': 'mb-3 form-control',
            }),
            'contenido': Textarea(attrs={
                'class': 'mb-3 form-control',
                'rows': 5,
            }),
            'imagen': TextInput(attrs={
                'class': 'form-control-file mb-3',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control mb-3'
            })
        }


class ConfirmarBorrado(forms.Form):
    confirmar = forms.BooleanField(initial=False, required=True, widget=forms.HiddenInput())