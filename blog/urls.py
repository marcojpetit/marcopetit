from django.urls import path
from blog.views import blog, crear_entrada, categorias, crear_categoria, etiquetas, crear_etiqueta

urlpatterns = [
    path('', blog, name='blog'),
    path('crear_entrada', crear_entrada),
    path('categorias', categorias),
    path('crear_categorías', crear_categoria),
    path('etiquetas', etiquetas),
    path('crear_etiqueta', crear_etiqueta),
    ]