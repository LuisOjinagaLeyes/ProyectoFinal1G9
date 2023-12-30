from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from apps.comentarios.models import Comentario

from .models import Noticia, Categoria
from .forms import Formulario_Noticia, Formulario_Modificar_Noticia, ConfirmarBorrado

from django.http import Http404
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required



# Create your views here.


def I_Noticias(request):
    contexto = {}
    categoria = Categoria.objects.all()
    contexto['categorias'] = categoria

    filtro = request.GET.get('categoria', None)
    orden = request.GET.get('orden', None)

    todas_n = Noticia.objects.all()
    categoria_select = None

    if filtro and filtro != '0':
        try:
            categoria_select = Categoria.objects.get(pk=filtro)
            todas_n = todas_n.filter(categoria=categoria_select)
        except Categoria.DoesNotExist:
            raise Http404("La categoria no existe")


    if orden == "ASC":
        todas_n = todas_n.order_by('creado')
    elif orden == "DSC":
        todas_n = todas_n.order_by('-creado')

    # Lógica de paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(todas_n, 15)  # Cantidad de noticias por página

    try:
        noticias_pagina = paginator.page(page)
    except PageNotAnInteger:
        noticias_pagina = paginator.page(1)
    except EmptyPage:
        # Redirección a la última página en caso de una página vacía
        query_params = f"?categoria={filtro or ''}&orden={orden or ''}"
        return redirect(reverse('noticias:i_noticias') + query_params + f"&page={paginator.num_pages}")

    noticias_mas_vistas = Noticia.objects.order_by('-vistas')[:5]
    contexto['noticias_pagina'] = noticias_pagina
    contexto['noticias_mas_vistas'] = noticias_mas_vistas
    # contexto['categoria_actual'] en None si no se selecciona una categoría (filtro es None o '0'). 
    contexto['categoria_actual'] = categoria_select if filtro else None 

    return render(request, 'noticias/index_noticias.html', contexto)


class Cargar_Noticia(CreateView):
    model = Noticia
    template_name = 'noticias/cargar_noticia.html'
    form_class = Formulario_Noticia
    success_url = reverse_lazy('noticias:i_noticias')
    @login_required
    def form_valid(self, form):
        noticia = form.save(commit=False)
        noticia.usuario = self.request.user
        return super(Cargar_Noticia, self).form_valid(form)
#BASADO EN CLASE
# class Detalle_Noticia(DetailView):
#     model = Noticia
#     template_name = 'noticias/detalle_noticia.html'

#BASADO EN FUNCION

def Detalle_noticia(request, pk):
	contexto = {}
	n = Noticia.objects.get(pk = pk)
	contexto['noticia'] = n

	com = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = com
	return render(request,'noticias/detalle_noticia.html', contexto)

#BASADO EN CLASE
# class DetalleNoticiaView(DetailView):
#     model = Noticia
#     template_name = 'noticias/detalle_noticia.html'
#     context_object_name = 'noticia'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comentarios'] = Comentario.objects.filter(noticia=self.object)
#         return context



class Modificar_Noticia(UpdateView, UserPassesTestMixin, LoginRequiredMixin ):
    model = Noticia
    template_name = 'noticias/modificar_noticia.html'
    form_class = Formulario_Modificar_Noticia
    # success_url = reverse_lazy('noticias:i_noticias')
    @login_required
    def get_success_url(self):
        return reverse_lazy('noticias:i_noticias')

class Borrar_Noticia(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model= Noticia
    template_name = 'noticias/noticia_confirm_delete.html'
    form_class = ConfirmarBorrado
    success_url = reverse_lazy('noticias:i_noticias')
    @login_required
    def form_valid(self, form):
        if form.cleaned.data['confirmar']:
            return super().form_valid(form)
        else:
            return self.form_valid(form)


def Noticias_Mas_Vistas(request):
    noticias_mas_vistas = Noticia.objects.order_by('-vistas')[:5]
    #filtro por dia
    noticias_dia = noticias_mas_vistas.filter(creado__gte=timezone.now() - timedelta(days=1))
    #filtro por semana
    noticias_semana = noticias_mas_vistas.filter(creado__gte=timezone.now() - timedelta(weeks=1))
    #filtro por mes
    noticias_mes = noticias_mas_vistas.filter(creado__month=timezone.now().month)
    #filtro por año
    noticias_anio = noticias_mas_vistas.filter(creado__year=timezone.now().year)
    
    contexto = {
        'noticias_mas_vistas': noticias_mas_vistas,
        'noticias_dia': noticias_dia,
        'noticias_semana': noticias_semana,
        'noticias_mes': noticias_mes,
        'noticias_anio': noticias_anio,
    }

    return render(request, 'noticias/index_noticias.html', contexto)


class BuscarNoticias(ListView):
    model = Noticia
    template_name = 'noticias/buscar_noticias.html'
    context_object_name = 'resultados'
    #paginate_by es para la cantidad de noticias por página  
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Noticia.objects.filter(
                Q(titulo__icontains=query) | Q(contenido__icontains=query)
            )
        return Noticia.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
