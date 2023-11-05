from django.urls import path
from blog.views import blog, entrada_crear, entrada_eliminar, entrada_actualizar, etiqueta_actualizar, categoria_actualizar, categoria_eliminar, etiqueta_eliminar, entrada, entradas, categorias, etiquetas

urlpatterns = [
    path('', blog, name='blog'),
    path('entrada_crear', entrada_crear, name='entrada_crear'),
    path('entrada/<int:id>', entrada, name="entrada"),
    path('entrada_eliminar/<int:id>', entrada_eliminar, name='entrada_eliminar'),
    path('entrada_actualizar/<int:id>', entrada_actualizar, name='entrada_actualizar'),
    path('entradas', entradas, name='entradas'),
    path('etiquetas', etiquetas, name='etiquetas'),
    path('etiqueta_eliminar/<int:id>', etiqueta_eliminar, name='etiqueta_eliminar'),
    path('etiqueta_actualizar/<int:id>', etiqueta_actualizar, name='etiqueta_actualizar'),
    path('categorias', categorias, name='categorias'),
    path('categoria_eliminar/<int:id>', categoria_eliminar, name='categoria_eliminar'),
    path('categoria_actualizar/<int:id>', categoria_actualizar, name='categoria_actualizar'),
    ]