from django.urls import path , include
from . import views

app_name = 'Usuarios'

urlpatterns = [
    path('', views.Usuarios, name="Usuarios"),#Ejemplo
    
    path('login/', views.Login, name ='login'),
    
    path('registro/', views.Registro, name = 'registro'),
]
