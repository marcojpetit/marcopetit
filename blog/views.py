from django.shortcuts import render, redirect
from blog.models import Categoria
from blog.forms import CrearCategoriaFormulario

def blog (request):
    return render(request, 'blog/blog.html', {})

def crear_entrada (request):
    return render(request, 'blog/crear_entrada.html', {})

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
         listado_categorias = Categoria.objects.filter(nombre=categoria_a_buscar.lower()) #pido una categoria en particular
    else:
        listado_categorias = Categoria.objects.all() #pido todos los registros del modelo

    return render(request, 'blog/categorias.html', {'formulario':formulario, 'listado_categorias':listado_categorias})

def etiquetas (request):
    return render(request, 'blog/etiquetas.html', {})