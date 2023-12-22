from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView, CreateView , DetailView , UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Noticia, Categoria
from .forms import Formulario_Noticia, Formulario_Modificar_Noticia



from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.
def I_Noticias(request):
    contexto = {}
    categoria = Categoria.objects.all()
    contexto['categorias'] = categoria
    filtro = request.GET.get('categoria', None)
    orden = request.GET.get('orden', None)

    if not filtro or filtro == '0':
        todas_n = Noticia.objects.all()
    else:
        categoria_select = Categoria.objects.get(pk = filtro)
        todas_n = Noticia.objects.filter(categoria = categoria_select)

    if orden == "ASC":
        todas_n = todas_n.order_by('creado')
    elif orden == "DSC":
        todas_n = todas_n.order_by('-creado')

#lógica de paginación
    page = request.GET.get('page', 1)
    paginator = Paginator(todas_n, 3) #cantidad de noticias por pagina
    try:
        noticias_pagina = paginator.page(page)
    except PageNotAnInteger:
        noticias_pagina = paginator.page(1)
    except EmptyPage:
        noticias_pagina = paginator.page(paginator.num_pages)

    contexto['noticia'] = noticias_pagina

    return render(request, 'noticias/index_noticias.html', contexto)


class Cargar_Noticia(CreateView):
    model = Noticia
    template_name = 'noticias/cargar_noticia.html'
    form_class = Formulario_Noticia
    success_url = reverse_lazy('noticias:i_noticias')

class Detalle_Noticia(DetailView):
    model = Noticia
    template_name = 'noticias/detalle_noticia.html'

class Modificar_Noticia(UpdateView):
    model = Noticia
    template_name = 'noticias/modificar_noticia.html'
    form_class = Formulario_Modificar_Noticia
    success_url = reverse_lazy('noticias:i_noticias')

class Borrar_Noticia(DeleteView):
    model= Noticia
    success_url = reverse_lazy('noticias:i_noticias')

