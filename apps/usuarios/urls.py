from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.Registro.as_view(), name = 'registro_user'),
]
