from django.urls import path
from blog.views import blog, crear_entrada, categorias, etiquetas

urlpatterns = [
    path('', blog, name='blog'),
    path('crear_entrada', crear_entrada, name='crear_entrada'),
    path('categorias', categorias, name='categorias'),
    path('etiquetas', etiquetas, name='etiquetas'),
    ]