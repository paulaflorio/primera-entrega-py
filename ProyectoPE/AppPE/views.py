from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def inicio(self):
    plantilla = loader.get_template('AppPE/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def series(request):
    return render(request, 'appPE/series.html')

def peliculas(request):
    return render(request, 'appPE/peliculas.html')

def libros(request):
    return render(request, 'appPE/libros.html')

def animes(request):
    return render(request, 'appPE/animes.html')

def mangas(request):
    return render(request, 'appPE/mangas.html')