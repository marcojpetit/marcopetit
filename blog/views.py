from django.shortcuts import render, redirect
from datetime import datetime
from blog.models import Entrada, Categoria, Etiqueta
from blog.forms import CrearEntradaFormulario, CrearCategoriaFormulario, CrearEtiquetaFormulario

def blog (request):
    listado_entradas = Entrada.objects.all() #pido todos los registros del modelo
    return render(request, 'blog/blog.html', {'listado_entradas':listado_entradas})

def crear_entrada (request):

    if request.method == 'POST': #si viene por POST crea el formulario con los datos
        formulario = CrearEntradaFormulario(request.POST, request.FILES)
        if formulario.is_valid(): #si el formulario tiene datos validos, crea y redirecciona a categorias
            titulo = formulario.cleaned_data.get('titulo')
            contenido = formulario.cleaned_data.get('contenido')
            imagen_portada = formulario.cleaned_data.get('imagen_portada')
            entrada = Entrada(id_categoria=1, titulo=titulo.lower(), contenido=contenido, id_autor=1, fecha_publicacion=datetime.now(), imagen_portada=imagen_portada)
            entrada.save()
            return redirect('entradas')
        else:#si el formulario no tiene datos validos, regresa al formulario y muestra los errores
            return render(request, 'blog/crear_entrada.html', {'formulario':formulario})
    formulario = CrearEntradaFormulario()  #si viene por GET por def
    return render(request, 'blog/crear_entrada.html', {'formulario':formulario})


def entradas (request):

    entrada_a_buscar = request.GET.get('entrada_a_buscar')

    if entrada_a_buscar:
         listado_entradas = Entrada.objects.filter(titulo__icontains=entrada_a_buscar.lower()) #pido una entrada en particular
    else:
        listado_entradas = Entrada.objects.all() #pido todos los registros del modelo

    return render(request, 'blog/entradas.html', {'listado_entradas':listado_entradas})

def entrada (request, id):
    entrada = Entrada.objects.get(id=id)
    return render(request, 'blog/entrada.html', {'entrada':entrada})


def categorias (request):

    if request.method == 'POST': #si viene por POST crea el formulario con los datos
        formulario = CrearCategoriaFormulario(request.POST)
        if formulario.is_valid(): #si el formulario tiene datos validos, crea y redirecciona a categorias
            nombre = formulario.cleaned_data.get('nombre')
            categoria = Categoria(nombre=nombre.lower())
            categoria.save()
            return redirect('categorias')
        
        else:#si el formulario no tiene datos validos, regresa al formulario y muestra los errores
            return render(request, 'blog/categorias.html', {'formulario':formulario})
        
    formulario = CrearCategoriaFormulario()  #si viene por GET por defecto crea el formulario vacio
    
    categoria_a_buscar = request.GET.get('categoria_a_buscar')

    if categoria_a_buscar:
         listado_categorias = Categoria.objects.filter(nombre__icontains=categoria_a_buscar.lower()) #pido una categoria en particular
    else:
        listado_categorias = Categoria.objects.all() #pido todos los registros del modelo

    return render(request, 'blog/categorias.html', {'formulario':formulario, 'listado_categorias':listado_categorias})

def etiquetas (request):

    if request.method == 'POST': #si viene por POST crea el formulario con los datos
        formulario = CrearEtiquetaFormulario(request.POST)
        if formulario.is_valid(): #si el formulario tiene datos validos, crea y redirecciona a categorias
            nombre = formulario.cleaned_data.get('nombre')
            etiqueta = Etiqueta(nombre=nombre.lower())
            etiqueta.save()
            return redirect('etiquetas')
        
        else:#si el formulario no tiene datos validos, regresa al formulario y muestra los errores
            return render(request, 'blog/etiquetas.html', {'formulario':formulario})
        
    formulario = CrearEtiquetaFormulario()  #si viene por GET por defecto crea el formulario vacio
    
    etiqueta_a_buscar = request.GET.get('etiqueta_a_buscar')

    if etiqueta_a_buscar:
         listado_etiquetas = Etiqueta.objects.filter(nombre__icontains=etiqueta_a_buscar.lower()) #pido una etiqueta en particular
    else:
        listado_etiquetas = Etiqueta.objects.all() #pido todos los registros del modelo

    return render(request, 'blog/etiquetas.html', {'formulario':formulario, 'listado_etiquetas':listado_etiquetas})