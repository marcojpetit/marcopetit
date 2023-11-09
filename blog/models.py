from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=30)

class Entrada(models.Model):
    id_categoria = models.IntegerField(default=1)
    #models.ForeignKey(Categoria, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=150)
    contenido = RichTextField()
    id_autor = models.IntegerField()
    fecha_publicacion = models.DateTimeField()
    imagen_portada = models.ImageField(upload_to="entradas", null=True, blank=True)

class Entrada_etiqueta(models.Model):
    id_entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)
    id_etiqueta = models.ForeignKey(Etiqueta, on_delete=models.PROTECT) 