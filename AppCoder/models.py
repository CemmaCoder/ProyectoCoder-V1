from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()

    def __str__(self):
        return f" Curso: {self.nombre} - Camada: {self.camada}"

# --------------------
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f" Estudiante: {self.apellido},{self.nombre} - Email: {self.email}"

# --------------------
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f" Profesor: {self.apellido},{self.nombre} - Email: {self.email} - Profesion: {self.profesion} "

# --------------------
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"Practico: {self.nombre} - Fecha de Entrega: {self.fechaDeEntrega} - Entregado: {self.entregado}"