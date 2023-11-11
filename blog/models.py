from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
    
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Entrada(models.Model):
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=150)
    sub_titulo = models.CharField(max_length=150, null=True)
    contenido = RichTextField()
    id_autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField()
    imagen_portada = models.ImageField(upload_to="entradas", null=True, blank=True)

class Entrada_etiqueta(models.Model):
    id_entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    id_etiqueta = models.ForeignKey(Etiqueta, on_delete=models.PROTECT) 