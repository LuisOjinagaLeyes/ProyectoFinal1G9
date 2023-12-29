from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registro_Form(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Ingrese su nombre',
                'class': 'mb-3 form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Ingrese su apellido',
                'class': 'mb-3 form-control',
            }),
            'username': forms.TextInput(attrs={
                'placeholder': 'Ingrese su nombre de usuario',
                'class': 'form-control-file mb-3',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Ingrese su correo electrónico',
                'class': 'form-control mb-3',
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': 'Ingrese su contraseña',
                'class': 'form-control mb-3',
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Ingrese su contraseña',
                'class': 'form-control mb-3',
            }),
        }