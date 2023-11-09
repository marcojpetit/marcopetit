from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth. decorators import login_required
from blog.models import Entrada, Categoria, Etiqueta
from blog.forms import CrearEntradaFormulario, CrearCategoriaFormulario, CrearEtiquetaFormulario, ActualizarEntradaFormulario, ActualizarEtiquetaFormulario, ActualizarCategoriaFormulario

def blog (request):
    listado_entradas = Entrada.objects.all() #pido todos los registros del modelo
    return render(request, 'blog/blog.html', {'listado_entradas':listado_entradas})

@login_required
def entrada_crear (request):
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
            return render(request, 'blog/entrada_crear.html', {'formulario':formulario})
    formulario = CrearEntradaFormulario()  #si viene por GET por def
    return render(request, 'blog/entrada_crear.html', {'formulario':formulario})


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

@login_required
def entrada_eliminar(request, id):
    entrada_a_eliminar = Entrada.objects.get(id=id)
    entrada_a_eliminar.delete()
    return redirect("entradas")

@login_required
def entrada_actualizar(request, id):
    entrada_a_actualizar = Entrada.objects.get(id=id)
    if request.method == "POST":
        formulario = ActualizarEntradaFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            entrada_a_actualizar.titulo = info_nueva.get('titulo')
            entrada_a_actualizar.contenido = info_nueva.get('contenido')
            entrada_a_actualizar.imagen_portada = info_nueva.get('imagen_portada')
            entrada_a_actualizar.save()
            #return redirect('entradas') Esto es si quiero que vaya al listado de entradas, pero yo lo cambie para que me vaya a la entrada actualizada
            entrada = Entrada.objects.get(id=id)
            return render(request, 'blog/entrada.html', {'entrada':entrada})
        return render(request, 'blog/entrada_actualizar.html', {'formulario':formulario})
    
    formulario = ActualizarEntradaFormulario(initial={'titulo': entrada_a_actualizar.titulo, 'contenido':entrada_a_actualizar.contenido, 'imagen_portada': entrada_a_actualizar.imagen_portada})
    return render(request, 'blog/entrada_actualizar.html', {'formulario':formulario})


@login_required
def categorias(request):
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
         listado_categorias = Categoria.objects.filter(nombre__icontains=categoria_a_buscar.lower()) #pido una etiqueta en particular
    else:
        listado_categorias = Categoria.objects.all() #pido todos los registros del modelo

    return render(request, 'blog/categorias.html', {'formulario':formulario, 'listado_categorias':listado_categorias})


@login_required
def categoria_actualizar(request,id):
    categoria_a_actualizar = Categoria.objects.get(id=id)
    if request.method == "POST":
        formulario = ActualizarCategoriaFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            categoria_a_actualizar.nombre = info_nueva.get('nombre')
            categoria_a_actualizar.save()
            return redirect('categorias')
        return render(request, 'blog/categoria_actualizar.html', {'formulario':formulario})
    
    formulario = ActualizarCategoriaFormulario(initial={'nombre': categoria_a_actualizar.nombre})
    return render(request, 'blog/categoria_actualizar.html', {'formulario':formulario})    

@login_required
def categoria_eliminar(request, id):
    categoria_a_eliminar = Categoria.objects.get(id=id)
    categoria_a_eliminar.delete()
    return redirect("categorias")


@login_required
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


@login_required
def etiqueta_actualizar(request, id):
    etiqueta_a_actualizar = Etiqueta.objects.get(id=id)
    if request.method == "POST":
        formulario = ActualizarEtiquetaFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            etiqueta_a_actualizar.nombre = info_nueva.get('nombre')
            etiqueta_a_actualizar.save()
            return redirect('etiquetas')
        return render(request, 'blog/etiqueta_actualizar.html', {'formulario':formulario})
    
    formulario = ActualizarEtiquetaFormulario(initial={'nombre': etiqueta_a_actualizar.nombre})
    return render(request, 'blog/etiqueta_actualizar.html', {'formulario':formulario})

@login_required
def etiqueta_eliminar(request, id):
    etiqueta_a_eliminar = Etiqueta.objects.get(id=id)
    etiqueta_a_eliminar.delete()
    return redirect("etiquetas")