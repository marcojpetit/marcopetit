from django.urls import path
from blog.views import blog, crear_entrada, entrada, entradas, categorias, etiquetas

urlpatterns = [
    path('', blog, name='blog'),
    path('entrada/<int:id>', entrada, name="entrada"),
    path('crear_entrada', crear_entrada, name='crear_entrada'),
    path('entradas', entradas, name='entradas'),
    path('categorias', categorias, name='categorias'),
    path('etiquetas', etiquetas, name='etiquetas'),
    ]