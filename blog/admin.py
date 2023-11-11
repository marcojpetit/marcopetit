from django.contrib import admin

from blog.models import Entrada, Categoria, Etiqueta

admin.site.register(Entrada)
admin.site.register(Categoria)
admin.site.register(Etiqueta)
