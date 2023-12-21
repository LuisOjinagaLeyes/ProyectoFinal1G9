from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.I_Noticias, name="i_noticias"),
    path('cargar/', views.Cargar_Noticia.as_view(), name="cargar_noticia"),
    path('detalle/<int:pk>', views.Detalle_Noticia.as_view(), name='detalle_noticia'),
    path('modificar/<int:pk>', views.Modificar_Noticia.as_view(), name='modificar_noticia'),
    path('borrar/<int:pk>', views.Borrar_Noticia.as_view(), name='borrar_noticia'),
]
