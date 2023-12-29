from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import DeleteView, UpdateView
from apps.noticias.models import Noticia
from .models import Comentario
from django.urls import reverse_lazy
from .forms import Form_Modificacion
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
@login_required
def Agregar_Comentario(request,pk):


	texto = request.POST.get('comentario',None)

	noticia = Noticia.objects.get(pk = pk)
	usuario = request.user
	Comentario.objects.create(texto = texto, usuario = usuario, noticia = noticia)

	return HttpResponseRedirect(reverse_lazy('noticias:detalle_noticia', kwargs = {'pk':pk}))


class BorrarComentario(DeleteView):
	model = Comentario
	def get_success_url(self):         
		return reverse_lazy('noticias:detalle_noticia',kwargs={'pk': self.object.noticia.pk})

class ModificarComentario(UpdateView):
	model = Comentario
	form_class = Form_Modificacion
	template_name = 'comentarios/modificar.html'
	def get_success_url(self):         
		return reverse_lazy('noticias:detalle_noticia',kwargs={'pk': self.object.noticia.pk})