from django.shortcuts import render

#vistas con clases de django
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from cursos.models import Curso

class Cursos(ListView):
    model = Curso
    context_object_name = 'listado_de_cursos'
    template_name = 'cursos/cursos.html'

class ListadoCursos(ListView):
    model = Curso
    context_object_name = 'listado_de_cursos'
    template_name = 'cursos/listado_cursos.html'
    
class CrearCurso(LoginRequiredMixin, CreateView):
    model = Curso
    template_name = 'cursos/crear_curso.html'
    fields = ['anio', 'mes', 'nombre', 'instituto', 'lugar', 'horas']
    success_url = reverse_lazy('listado_cursos')

class DetalleCurso(DetailView):
    model = Curso
    template_name = 'cursos/detalle_curso.html'
    
class EditarCurso(LoginRequiredMixin, UpdateView):
    model = Curso
    template_name = 'cursos/editar_curso.html'
    fields = ['anio', 'mes', 'nombre', 'instituto', 'lugar', 'horas']
    success_url = reverse_lazy('listado_cursos')

class EliminarCurso(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'cursos/eliminar_curso.html'
    success_url = reverse_lazy('listado_cursos')

