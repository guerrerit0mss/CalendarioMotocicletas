from django.template import Template,context,loader
from django.shortcuts import render
from trivias.models import *
import random



# Create your views here.

def trivias(request):
   numeroPreg=1
   if request.method == 'GET':            
      numeroPreg=request.GET.get('qstn')             
      puntaje=request.GET.get('pntj')    
      hora=request.GET.get('hora')
      user=request.GET.get('user')

      
  
   datos={"contexto": ordenarPreguntas(numeroPreg)}   
   return  render(request,"home.html",datos)

def iniciaSesion(request):

   return  render(request,"iniciaSesion.html")

def ordenarPreguntas(numeroPregunta):   
   #Se hace la query para preguntas
   preg= preguntas.objects.filter(id=numeroPregunta)

   #Se hace la query para respuestas
   resp= respuestas.objects.filter(pregunta=numeroPregunta)

   #Se asigna el id de la categoria a la variable categ
   for cate in preg:
      id_preg=cate.categoria
   categ=categorias.objects.filter(id=id_preg)

   #Se ordenan los valores de las respuestas tanto el texto como si es la correcta
   resp_ord= []
   for respuesta in resp:
      resp_ord.append([respuesta.texto, respuesta.acierto])
   random.shuffle(resp_ord)#desordeno las respuestas
   sigPreg=int(numeroPregunta)+1

   contex={"preguntas":preg, "respuestas":resp_ord, "categoria": categ, "Npreg":sigPreg}#armo el diccionario a enviar  
  
   return contex

