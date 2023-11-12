from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.contrib.auth. decorators import login_required
from blog.models import Entrada, Categoria, Etiqueta
from django.contrib.auth.models import User
from django.db.models import ProtectedError

from blog.forms import CrearEntradaFormulario, CrearCategoriaFormulario, CrearEtiquetaFormulario, ActualizarEntradaFormulario, ActualizarEtiquetaFormulario, ActualizarCategoriaFormulario

def blog (request):
    listado_entradas = Entrada.objects.all() #pido todos los registros del modelo
    return render(request, 'blog/blog.html', {'listado_entradas':listado_entradas})

@login_required
def entrada_crear (request):
    formulario = CrearEntradaFormulario()  #si viene por GET por def
    if request.method == 'POST': #si viene por POST crea el formulario con los datos
        formulario = CrearEntradaFormulario(request.POST, request.FILES)
        if formulario.is_valid(): #si el formulario tiene datos validos, crea y redirecciona a categorias
            id_categoria = formulario.cleaned_data.get('id_categoria')
            titulo = formulario.cleaned_data.get('titulo')
            sub_titulo = formulario.cleaned_data.get('sub_titulo')
            contenido = formulario.cleaned_data.get('contenido')
            id_autor = User.objects.get(id=request.user.id)   
            imagen_portada = formulario.cleaned_data.get('imagen_portada')
            etiquetas = formulario.cleaned_data.get('etiquetas')
            entrada = Entrada(id_categoria=id_categoria, titulo=titulo.lower(), sub_titulo=sub_titulo.lower(), contenido=contenido, id_autor=id_autor, fecha_publicacion=datetime.now(), imagen_portada=imagen_portada)
            entrada.save()
            entrada.etiquetas.set(etiquetas)
            return redirect('entradas')
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
    autor = User.objects.get(id=entrada.id_autor.id)
    return render(request, 'blog/entrada.html', {'entrada':entrada, 'autor':autor,})

@login_required
def entrada_eliminar(request, id):
    entrada_a_eliminar = Entrada.objects.get(id=id)
    entrada_a_eliminar.delete()
    return redirect("entradas")

@login_required
def entrada_actualizar(request, id):
    entrada_a_actualizar = Entrada.objects.get(id=id)
    
    formulario = ActualizarEntradaFormulario(initial={'id_categoria':entrada_a_actualizar.id_categoria, 'titulo': entrada_a_actualizar.titulo, 'sub_titulo': entrada_a_actualizar.sub_titulo, 'contenido':entrada_a_actualizar.contenido, 'imagen_portada': entrada_a_actualizar.imagen_portada, 'etiquetas':entrada_a_actualizar.etiquetas.all()})
    if request.method == "POST":
        formulario = ActualizarEntradaFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            entrada_a_actualizar.id_categoria = info_nueva.get('id_categoria')
            entrada_a_actualizar.titulo = info_nueva.get('titulo')
            entrada_a_actualizar.sub_titulo = info_nueva.get('sub_titulo')
            entrada_a_actualizar.contenido = info_nueva.get('contenido')
            if info_nueva.get('imagen_portada'):
                entrada_a_actualizar.imagen_portada = info_nueva.get('imagen_portada')
            
            etiquetas = info_nueva.get('etiquetas')
            entrada_a_actualizar.save()
            entrada_a_actualizar.etiquetas.set(etiquetas)
            #return redirect('entradas') Esto es si quiero que vaya al listado de entradas, pero yo lo cambie para que me vaya a la entrada actualizada
            entrada = Entrada.objects.get(id=id)
            return render(request, 'blog/entrada.html', {'entrada':entrada})    
    
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
    try:
        categoria_a_eliminar = Categoria.objects.get(id=id)
        categoria_a_eliminar.delete()
        return redirect("categorias")
    except ProtectedError as e:
        return render(request, 'blog/categoria_eliminar_error.html', {'e':e})



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