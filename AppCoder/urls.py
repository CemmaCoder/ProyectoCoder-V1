from django.urls import path
from AppCoder.views import Curso, Estudiante, Profesor, Entregable, Inicio

urlpatterns = [
    path("", Inicio,name='Inicio'),
    path("Curso/", Curso,name='Curso'),
    path("Estudiante/", Estudiante,name='Estudiante'),
    path("Profesor/", Profesor,name='Profesor'),
    path("Entregable/", Entregable,name='Entregable'),
    ]