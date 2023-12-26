from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, CreateView , DetailView , UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Noticia, Categoria
from .forms import Formulario_Noticia, Formulario_Modificar_Noticia

from django.http import Http404
from django.utils import timezone
from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.
def I_Noticias(request):
    contexto = {}
    categoria = Categoria.objects.all()
    contexto['categorias'] = categoria

    filtro = request.GET.get('categoria', None)
    orden = request.GET.get('orden', None)

    todas_n = Noticia.objects.all()

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

    contexto['noticias_pagina'] = noticias_pagina
    # contexto['categoria_actual'] en None si no se selecciona una categoría (filtro es None o '0'). 
    contexto['categoria_actual'] = categoria_select if filtro else None 

    return render(request, 'noticias/index_noticias.html', contexto)
# def I_Noticias(request):
#     contexto = {}
#     categoria = Categoria.objects.all()
#     contexto['categorias'] = categoria
    
#     filtro = request.GET.get('categoria', None)
#     orden = request.GET.get('orden', None)

#     if not filtro or filtro == '0':
#         todas_n = Noticia.objects.all()
#     else:
#         categoria_select = Categoria.objects.get(pk = filtro)
#         todas_n = Noticia.objects.filter(categoria = categoria_select)

#     if orden == "ASC":
#         todas_n = todas_n.order_by('creado')
#     elif orden == "DSC":
#         todas_n = todas_n.order_by('-creado')

# #lógica de paginación
#     page = request.GET.get('page', 1)
#     paginator = Paginator(todas_n, 3) #cantidad de noticias por pagina
#     try:
#         noticias_pagina = paginator.page(page)
#     except PageNotAnInteger:
#         noticias_pagina = paginator.page(1)
#     except EmptyPage:
#         noticias_pagina = paginator.page(paginator.num_pages)
#         return redirect(reverse('noticias:i_noticias') + f"?categoria={filtro or ''}&orden={orden or ''}&page={paginator.num_pages}")

#     contexto['noticias_pagina'] = noticias_pagina

#     return render(request, 'noticias/index_noticias.html', contexto)


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

    return render(request, 'noticias/index_noticias.html', {'noticias_mas_vistas': noticias_mas_vistas, 'noticias_dia': noticias_dia, 'noticias_semana': noticias_semana, 'noticias_mes': noticias_mes, 'noticias_anio': noticias_anio, })

