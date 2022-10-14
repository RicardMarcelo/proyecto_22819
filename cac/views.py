from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django')

def mundial(request):
    return HttpResponse('VAMOS ARGENTINA')

def saludar(request,nombre='Estimada Persona'):
    return HttpResponse(f"""
    <h1>Hola Mundo Django - {nombre}</h1>
    <p>Estoy haciendo mi primera prueba</p>
    """)

def ver_proyectos(request,año,mes):
    return HttpResponse(f"""
    <h1>Proyectos del - {mes}/{año}</h1>
    <p>Listado de proyectos</p>
    """)