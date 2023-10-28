from django.shortcuts import render

def blog (request):
    return render(request, 'blog/blog.html', {})

def crear_entrada (request):
    return render(request, 'blog/crear_entrada.html', {})

def categorias (request):
    return render(request, 'blog/categorias.html', {})

def crear_categoria (request):
    return render(request, 'blog/crear_categoria.html', {})

def etiquetas (request):
    return render(request, 'blog/etiquetas.html', {})

def crear_etiqueta (request):
    return render(request, 'blog/crear_etiqueta.html', {})

