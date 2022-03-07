from django.template import Template,context,loader
from django.shortcuts import render
from trivias.models import *
import random



# Create your views here.

def trivias(request):
   numeroPreg=1
   if request.method == 'GET':      
      horas=request.GET.get('hora')        
      numeroPreg=request.GET.get('qstn')             
      puntaje=request.GET.get('pntj')  
      user=request.GET.get('user')      
      #Comprobacion para finalizar trivia e ir a tabla de posiciones
      if int(numeroPreg)==3:         
         datos={"user":user,"hora":horas, "puntaje":puntaje}
         return  render(request,"final.html",datos)      
   
   datos={"contexto": ordenarPreguntas(numeroPreg, user, horas, puntaje)}   
   return  render(request,"home.html",datos)



def ordenarPreguntas(numeroPregunta, user, horas, puntaje):   
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

   contex={"preguntas":preg, "respuestas":resp_ord, "categoria": categ, "Npreg":sigPreg, "user":user, "puntaje":puntaje, "hora":horas}#armo el diccionario a enviar  
  
   return contex

def iniciaSesion(request):
   return  render(request,"iniciaSesion.html")
