from django.db import models
from django import forms
from django.contrib.auth.models import User
from apps.noticias.models import Noticia

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
