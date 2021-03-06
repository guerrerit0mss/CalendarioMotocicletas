
from django.db import models

# Create your models here.

class categorias(models.Model):
    nombre=models.CharField(max_length=20, null=False)

class usuario(models.Model):
    nombre=models.CharField(max_length=20, null=False)
    tiempo=models.IntegerField( null=False)
    fechaCreacion=models.DateField(null=False)

class preguntas(models.Model):
    texto=models.CharField(max_length=30, null=False)
    categoria=models.IntegerField(null=False)
    imagen=models.URLField(max_length=50, null=True)

class respuestas(models.Model):
    texto=models.CharField(max_length=20, null=False)
    pregunta=models.IntegerField(null=False)
    acierto=models.BooleanField(null=False)