from django.shortcuts import render
from apps.noticias.models import Categoria

def Base(request):

	return render(request,'base.html')

def Index(request):
    
    categorias = Categoria.objects.all()
    
    return render(request,'index.html', {'categorias': categorias})

def Detalle_Noticia(request):

    return render(request,'detalle_noticia.html')

def Login(request):

    return render(request,'login.html')

def Registro(request):

    return render(request,'registro.html')


def Blog(request):

    return render(request,'blog.html')

def Contacto(request):

    return render(request,'contacto.html')

def Search_Result(request):

    return render(request,'search-result.html')

