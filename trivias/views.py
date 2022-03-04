from django.template import Template,context,loader
from django.shortcuts import render
from trivias.models import *
import random



# Create your views here.

def trivias(request):
   datos={"categoria" : "Arte", "contexto": ordenarPreguntas(1)}   
   return  render(request,"home.html",datos)

def ordenarPreguntas(numeroPregunta):   
   preg= preguntas.objects.filter(id=numeroPregunta)
   resp=respuestas.objects.filter(pregunta=numeroPregunta)
   for cate in preg:
      id_preg=cate.categoria
   categ=categorias.objects.filter(id=id_preg)
   resp_ord= []

   for respuesta in resp:
      resp_ord.append([respuesta.texto, respuesta.acierto])

   random.shuffle(resp_ord)
   contex={"preguntas":preg, "respuestas":resp_ord, "categoria": categ }  
   return contex

