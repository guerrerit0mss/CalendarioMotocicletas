from django.template import Template,context,loader
from django.shortcuts import render, HttpResponse



def Home(request):
    horaInicio=8
    horaFin=20
    lineas=[]
    i=horaInicio
    while i <= horaFin:
        lineas.append(i)
        i=i+1

    datos={"cant_motos": 8, "horaInicio": 8, "lineas":lineas}
   
    return  render(request,"home.php",datos)