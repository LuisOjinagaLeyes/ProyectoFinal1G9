from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views 


app_name = 'noticias'

urlpatterns = [
    path('', views.I_Noticias, name="i_noticias"),
    path('cargar/', views.Cargar_Noticia.as_view(), name="cargar_noticia"),
    path('detalle/<int:pk>', views.Detalle_Noticia.as_view(), name='detalle_noticia'),
    path('modificar/<int:pk>', views.Modificar_Noticia.as_view(), name='modificar_noticia'),
    path('borrar/<int:pk>', views.Borrar_Noticia.as_view(), name='borrar_noticia'),
    # path('noticias_mas_vistas/', views.Noticias_Mas_Vistas, name='noticias_mas_vistas'),
]
