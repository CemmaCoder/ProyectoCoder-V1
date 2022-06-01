from django.shortcuts import HttpResponse, render
from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from django.template import loader

def Curso(request):
    return render(request, 'appCoder/Curso.html')

def Estudiante(request):
    return render(request, 'appCoder/Estudiante.html')

def Profesor(request):
    return render(request, 'appCoder/Profesor.html')

def Entregable(request):
    return render(request, 'appCoder/Entregable.html')

def Inicio(self):
    plantilla = loader.get_template("AppCoder/inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)
