from django.urls import path
from cursos.views import Cursos, ListadoCursos, CrearCurso, DetalleCurso, EditarCurso, EliminarCurso

urlpatterns = [
    path('', Cursos.as_view(), name='cursos'),
    path('listado', ListadoCursos.as_view(), name='listado_cursos'),
    path('crear/', CrearCurso.as_view(), name='crear_curso'),
    path('curso/<int:pk>', DetalleCurso.as_view(), name='detalle_curso'),
    path('editar/<int:pk>', EditarCurso.as_view(), name='editar_curso'),
    path('eliminar/<int:pk>', EliminarCurso.as_view(), name='eliminar_curso'),
    ]