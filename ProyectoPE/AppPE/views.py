from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppPE.models import Serie, Pelicula, Libro, Anime, Manga
from AppPE.forms import SerieFormulario, PeliculaFormulario, LibroFormulario, AnimeFormulario, MangaFormulario

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

def serieFormulario(request):
    if request.method == 'POST':
        miFormulario = SerieFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            temporadas =  informacion['temporadas']
            episodios =  informacion['episodios']
            añoEstreno =  informacion['añoEstreno']
            director =  informacion['director']
            serie = Serie(nombre = nombre, temporadas = temporadas, episodios = episodios, añoEstreno = añoEstreno, director = director)
            serie.save()
        return render(request, 'AppPE/inicio.html')
    else:
        miFormulario = SerieFormulario()
    return render(request, 'appPE/serieFormulario.html', {'miFormulario': miFormulario})

def peliculaFormulario(request):
    if request.method == 'POST':
        miFormulario = PeliculaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            duracion =  informacion['duracion']
            añoEstreno =  informacion['añoEstreno']
            director =  informacion['director']
            pelicula = Pelicula(nombre = nombre, duracion = duracion, añoEstreno = añoEstreno, director = director)
            pelicula.save()
        return render(request, 'AppPE/inicio.html')
    else:
        miFormulario = PeliculaFormulario()
    return render(request, 'appPE/peliculaFormulario.html', {'miFormulario': miFormulario})

def libroFormulario(request):
    if request.method == 'POST':
        miFormulario = LibroFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            añoPublicacion =  informacion['añoPublicacion']
            paginas =  informacion['paginas']
            autor =  informacion['autor']
            libro = Libro(nombre = nombre, añoPublicacion = añoPublicacion, paginas = paginas, autor = autor)
            libro.save()
        return render(request, 'AppPE/inicio.html')
    else:
        miFormulario = LibroFormulario()
    return render(request, 'appPE/libroFormulario.html', {'miFormulario': miFormulario})

def animeFormulario(request):
    if request.method == 'POST':
        miFormulario = AnimeFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            temporadas =  informacion['temporadas']
            episodios =  informacion['episodios']
            añoEstreno =  informacion['añoEstreno']
            director =  informacion['director']
            anime = Anime(nombre = nombre, temporadas = temporadas, episodios = episodios, añoEstreno = añoEstreno, director = director)
            anime.save()
        return render(request, 'AppPE/inicio.html')
    else:
        miFormulario = SerieFormulario()
    return render(request, 'appPE/animeFormulario.html', {'miFormulario': miFormulario})

def mangaFormulario(request):
    if request.method == 'POST':
        miFormulario = MangaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            añoPublicacion =  informacion['añoPublicacion']
            paginas =  informacion['paginas']
            autor =  informacion['autor']
            manga = Manga(nombre = nombre, añoPublicacion = añoPublicacion, paginas = paginas, autor = autor)
            manga.save()
        return render(request, 'AppPE/inicio.html')
    else:
        miFormulario = MangaFormulario()
    return render(request, 'appPE/mangaFormulario.html', {'miFormulario': miFormulario})
