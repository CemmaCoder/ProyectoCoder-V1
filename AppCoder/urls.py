from django.urls import path
from AppCoder.views import CursoView, EstudianteView, ProfesorView, EntregableView

urlpatterns = [
    path("Curso/", CursoView),
    path("Estudiante/", EstudianteView),
    path("Profesor/", ProfesorView),
    path("Entregable/", EntregableView)
]