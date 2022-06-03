from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicioView,name='Inicio'),
    path("Curso/", cursoView,name='Curso'),
    path("Estudiante/", estudianteView,name='Estudiante'),
    path("Profesor/", profesorView,name='Profesor'),
    path("Entregable/", entregableView,name='Entregable'),
    path("CursoFormulario/", cursoFormularioView,name='CursoFormulario'),
    path("EstudianteFormulario/", estudianteFormularioView,name='EstudianteFormulario'),
    path("ProfesorFormulario/", profesorFormularioView,name='ProfesorFormulario'),
    path("EntregableFormulario/", entregableFormularioView,name='EntregableFormulario'),
    ]