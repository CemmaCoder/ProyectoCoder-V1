from django.shortcuts import HttpResponse, render
from AppCoder.models import *
from django.template import loader
from .forms import *

def inicioView(self):
    plantilla = loader.get_template("AppCoder/inicio.html")
    documento = plantilla.render()
    return HttpResponse(documento)

def cursoView(request):
    return render(request, 'appCoder/Curso.html')

def estudianteView(request):
    return render(request, 'appCoder/Estudiante.html')

def profesorView(request):
    return render(request, 'appCoder/Profesor.html')

def entregableView(request):
    return render(request, 'appCoder/Entregable.html')

def cursoFormularioView(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        camada = informacion['camada']
        curso = Curso(nombre=nombre, camada=camada)
        curso.save()
        return render(request, 'appCoder/inicio.html')
    else:
        miFormulario=CursoFormulario()
    return render(request, 'appCoder/cursoFormulario.html', {"miFormulario":miFormulario})

def estudianteFormularioView(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']
        estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email)
        estudiante.save()
        return render(request, 'appCoder/inicio.html')
    else:
        miFormulario=EstudianteFormulario()
    return render(request, 'appCoder/estudianteFormulario.html', {"miFormulario":miFormulario})

def profesorFormularioView(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']
        profesion = informacion['profesion']
        profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
        profesor.save()
        return render(request, 'appCoder/inicio.html')
    else:
        miFormulario=ProfesorFormulario()
    return render(request, 'appCoder/profesorFormulario.html', {"miFormulario":miFormulario})

def entregableFormularioView(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['nombre']
        fechaDeEntrega = informacion['fechaDeEntrega']
        entregado = informacion['entregado']
        entregable = Entregable(nombre=nombre, fechaDeEntrega=fechaDeEntrega, entregado=entregado)
        entregable.save()
        return render(request, 'appCoder/inicio.html')
    else:
        miFormulario=EntregableFormulario()
    return render(request, 'appCoder/entregableFormulario.html', {"miFormulario":miFormulario})