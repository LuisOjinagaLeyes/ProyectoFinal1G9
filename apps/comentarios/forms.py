from django import forms
from .models import Comentario
# from django.forms import Textarea

class Form_Modificacion(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('texto',)