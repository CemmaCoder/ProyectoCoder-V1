from datetime import datetime
from django.shortcuts import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor, Entregable
from django.template import loader
import datetime

def CursoView(self):
    curso = Curso(nombre="Javascript",camada=32075)
    curso.save()
    documento1 = f"Curso {curso.nombre} - Camada {curso.camada}"
    return HttpResponse(documento1)

def EstudianteView(self):
    estudiante = Estudiante(nombre="Emmanuel", apellido="Leiva", email= "cemmanueleiva@gmail.com",)
    estudiante.save()
    documento2= f"Estudiante {estudiante.apellido}, {estudiante.nombre} - Email = {estudiante.email}"
    return HttpResponse(documento2)

def ProfesorView(self):
    profesor = Profesor(nombre="Octavio", apellido="Lafourcade", email="Sin especificar", profesion="Maestro")
    profesor.save()
    documento3 = f"Profesor {profesor.apellido}, {profesor.nombre} - Email = {profesor.email} - Profesion = {profesor.profesion}"
    return HttpResponse(documento3)

def EntregableView(self):
    entregable = Entregable(nombre="Trabajo Practico", fechaDeEntrega=datetime.datetime.now(), entregado=True)
    entregable.save()
    documento4 = f"Entregable {entregable.nombre} - Fecha de entrega: {entregable.fechaDeEntrega} - Entregado {entregable.entregado}"
    return HttpResponse(documento4)

def miPlantilla(self):
    plantilla = loader.get_template("plantilla.html")
    documento = plantilla.render()
    return HttpResponse(documento)
