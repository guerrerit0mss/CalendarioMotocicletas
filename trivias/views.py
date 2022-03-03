from django.template import Template,context,loader
from django.shortcuts import render, HttpResponse



# Create your views here.

def trivias(request):
   datos={"pregunta1":"pregunta 1", 
   "respuesta1" : "respuesta numero 1",
   "respuesta2" : "respuesta 2",
   "respuesta3" : "respuesta 3",
   "respuesta4" : "respuesta 4", 
   "categoria" : "categoria",
   "imagen": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Leonardo_da_Vinci_-_Mona_Lisa_%28Louvre%2C_Paris%29.jpg/800px-Leonardo_da_Vinci_-_Mona_Lisa_%28Louvre%2C_Paris%29.jpg"
   }
   
   return  render(request,"home.html",datos)
