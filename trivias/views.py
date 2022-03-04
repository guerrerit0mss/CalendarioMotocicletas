from django.template import Template,context,loader
from django.shortcuts import render
from trivias.models import *



# Create your views here.

def trivias(request):
   datos={
   "pregunta":"¿Quién pintó esta obra de arte?", 
   "categoria" : "Arte",
   "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Leonardo_da_Vinci_-_Mona_Lisa_%28Louvre%2C_Paris%29.jpg/800px-Leonardo_da_Vinci_-_Mona_Lisa_%28Louvre%2C_Paris%29.jpg",
   "contexto": ordenarPreguntas(1)
   }
   
   return  render(request,"home.html",datos)

def ordenarPreguntas(numeroPregunta):   
   preg= preguntas.objects.filter(id=numeroPregunta)
   resp=respuestas.objects.filter(pregunta=1)
   resp_ord= []

   for respuesta in resp:
      resp_ord.append([respuesta.texto, respuesta.acierto])

   contex={"preguntas":preg, "respuestas":resp_ord}   
   return contex

