from django import forms
from .models import Noticia

class Formulario_Noticia(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields =['titulo','contenido','imagen','categoria']

class Formulario_Modificar_Noticia(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields =['titulo','contenido','imagen','categoria']

        def __init__(self, *args, **kwargs):
            super(Formulario_Modificar_Noticia, self).__init__(*args, **kwargs)
            
            for field_name, field in self.fields.items():
                field.widget.attrs.update({'class': 'form-control'})
                
                if field_name == 'imagen':
                    field.widget.attrs.update({'class': 'form-control-file'})
                
                if field_name == 'titulo':
                    field.widget.attrs.update({'placeholder': 'Ingrese el titulo'})


class ConfirmarBorrado(forms.Form):
    confirmar = forms.BooleanField(initial=False, required=True, widget=forms.HiddenInput())