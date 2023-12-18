from django.urls import path , include
from . import views

app_name = 'inicio_portadas'

urlpatterns = [
    path('', views.Inicio_Portadas, name="I_Portadas"),#Ejemplo
]
