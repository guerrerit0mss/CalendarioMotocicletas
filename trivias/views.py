from django.template import Template,context,loader
from django.shortcuts import render, HttpResponse



# Create your views here.

def Home(request):
   datos={"pregunta":1}
   
    return  render(request,"templates/home.php",datos)
