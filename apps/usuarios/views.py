from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import Registro_Form

# Create your views here.
# def Usuarios(request):

#     return render(request, 'usuarios')

# def Login(request):

#     return render(request,'usuarios/login.html')

# def Registro(request):

#     return render(request,'usuarios/registro.html')

class Registro(CreateView):
    form_class = Registro_Form
    success_url = reverse_lazy('login')
    template_name = 'usuarios/registro.html'