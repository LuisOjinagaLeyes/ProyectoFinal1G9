from django.shortcuts import render

# Create your views here.
def Inicio_Portadas(request):

    return render(request, 'inicio_portadas/index_inicio_portadas.html')