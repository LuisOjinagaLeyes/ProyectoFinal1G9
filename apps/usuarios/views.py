from django.shortcuts import render

# Create your views here.
def Usuarios(request):

    return render(request, 'usuarios')

def Login(request):

    return render(request,'usuarios/login.html')

def Registro(request):

    return render(request,'usuarios/registro.html')