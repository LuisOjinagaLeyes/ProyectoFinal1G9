from django.db import models
from django import forms
from django.contrib.auth.models import User
from apps.noticias.models import Noticia

# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User

class Comentario(models.Model):
	creado = models.DateTimeField(
		'creado',
		auto_now_add=True
	)
	modificado = models.DateTimeField(
		'modificado',
		auto_now=True
	)
	texto = models.TextField()
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)
	noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.texto

class Form_Modificacion(forms.ModelForm):

	class Meta:
		model = Comentario
		fields = ('texto',)
		widgets = {
			'texto': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu comentario...', 'required': 'true'}),
		}

# from django import forms
# from .models import Comment

# class CommentForm(forms.ModelForm):
#     content = forms.CharField(label ="", widget = forms.Textarea(
#     attrs ={
#         'class':'form-control',
#         'placeholder':'Comment here !',
#         'rows':4,
#         'cols':50
#     }))
#     class Meta:
#         model = Comment
#         fields =['content']