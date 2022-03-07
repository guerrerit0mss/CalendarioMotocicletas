from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('preguntas/', views.trivias),
    path('IniciaSesion/', views.iniciaSesion),
]