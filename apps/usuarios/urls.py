from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usuarios'

urlpatterns = [
    # path('', views.Usuarios, name="Usuarios"),
    
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    
    path('registro/', views.Registro.as_view(), name = 'registro_user'),

]
