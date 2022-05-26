from django.contrib import admin
from django.urls import path
from AppCoder.views import CursoView
from AppCoder.views import EstudianteView
from AppCoder.views import ProfesorView
from AppCoder.views import EntregableView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("Curso/", CursoView),
    path("Estudiante/", EstudianteView),
    path("Profesor/", ProfesorView),
    path("Entregable/", EntregableView)
]
