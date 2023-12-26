from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):

    creado = models.DateTimeField('creado', auto_now_add=True)
    modificado= models.DateTimeField('modificado', auto_now=True)
    
    vistas = models.IntegerField(default=0)
    
    titulo = models.CharField(max_length = 255)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to = 'noticias')
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, default=1)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.titulo