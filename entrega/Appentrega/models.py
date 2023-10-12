from django.db import models


class Students(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def _str_(self) -> str:
        return f"Nombre: {self.nombre} - Camada: {self.camada}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
  

class Entregables(models.Model):
    nombre = models.CharField(max_length=40)
    FechaEntrega = models.DateField()
    entregado = models.BooleanField()