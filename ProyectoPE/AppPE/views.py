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

def busquedaPeliculaDirector(request):
    return render(request, 'appPE/busquedaPeliculaDirector.html')

def buscarPeliculaDirector(request):
    # respuesta = f"Se encontro el director {request.GET['director']}"
    if request.GET['director']:
        director = request.GET['director']
        peliculas = Pelicula.objects.filter(director = director)
        return render(request, 'appPE/resultadosBusquedaPeliculaDirector.html', {'peliculas': peliculas, 'director': director})
    else:
        respuesta = "No se han ingresado datos"
    return HttpResponse(respuesta)

def busquedaPeliculaAño(request):
    return render(request, 'appPE/busquedaPeliculaAño.html')

def buscarPeliculaAño(request):
    if request.GET['añoEstreno']:
        añoEstreno = request.GET['añoEstreno']
        peliculas = Pelicula.objects.filter(añoEstreno = añoEstreno)
        return render(request, 'appPE/resultadosBusquedaPeliculaAño.html', {'peliculas': peliculas, 'añoEstreno': añoEstreno})
    else:
        respuesta = "No se han ingresado datos"
    return HttpResponse(respuesta)


def busquedaSerieDirector(request):
    return render(request, 'appPE/busquedaSerieDirector.html')

def buscarSerieDirector(request):
    if request.GET['director']:
        director = request.GET['director']
        series = Serie.objects.filter(director = director)
        return render(request, 'appPE/resultadosSerieDirector.html', {'series': series, 'director': director})
    else:
        respuesta = "No se han ingresado datos"
    return HttpResponse(respuesta)

def busquedaSerieAño(request):
    return render(request, 'appPE/busquedaSerieAño.html')

def buscarSerieAño(request):
    if request.GET['añoEstreno']:
        añoEstreno = request.GET['añoEstreno']
        series = Serie.objects.filter(añoEstreno = añoEstreno)
        return render(request, 'appPE/resultadosSerieAño.html', {'series': series, 'añoEstreno': añoEstreno})
    else:
        respuesta = "No se han ingresado datos"
    return HttpResponse(respuesta)


def busquedaLibroAutor(request):
    return render(request, 'appPE/busquedaLibroAutor.html')

def buscarLibroAutor(request):
    if request.GET['autor']:
        autor = request.GET['autor']
        libros = Libro.objects.filter(autor = autor)
        return render(request, 'appPE/resultadosLibroAutor.html', {'libros': libros, 'autor': autor})
    else:
        respuesta = "No se han ingresado datos"
    return HttpResponse(respuesta)

def busquedaLibroAño(request):
    return render(request, 'appPE/busquedaLibroAño.html')

def buscarLibroAño(request):
    if request.GET['añoPublicacion']:
        añoPublicacion = request.GET['añoPublicacion']
        libros = Libro.objects.filter(añoPublicacion = añoPublicacion)
        return render(request, 'appPE/resultadosLibroAño.html', {'libros': libros, 'añoPublicacion': añoPublicacion})
    else:
        respuesta = "No se han ingresado datos"
    return HttpResponse(respuesta)


def busquedaMangaAutor(request):
    return render(request, 'appPE/busquedaMangaAutor.html')

def buscarMangaAutor(request):
    if request.GET['autor']:
        autor = request.GET['autor']
        mangas = Manga.objects.filter(autor = autor)
        return render(request, 'appPE/resultadosMangaAutor.html', {'mangas': mangas, 'autor': autor})
    else:
        respuesta = "No se han ingresado datos"
    return HttpResponse(respuesta)

def busquedaMangaAño(request):
    return render(request, 'appPE/busquedaMangaAño.html')

def buscarMangaAño(request):
    if request.GET['añoPublicacion']:
        añoPublicacion = request.GET['añoPublicacion']
        mangas = Manga.objects.filter(añoPublicacion = añoPublicacion)
        return render(request, 'appPE/resultadosMangaAño.html', {'mangas': mangas, 'añoPublicacion': añoPublicacion})
    else:
        respuesta = "No se han ingresado datos"
    return HttpResponse(respuesta)



def busquedaAnimeDirector(request):
    return render(request, 'appPE/busquedaAnimeDirector.html')

def buscarAnimeDirector(request):
    if request.GET['director']:
        director = request.GET['director']
        animes = Anime.objects.filter(director = director)
        return render(request, 'appPE/resultadosAnimeDirector.html', {'animes': animes, 'director': director})
    else:
        respuesta = "No se han ingresado datos"
    return HttpResponse(respuesta)

def busquedaAnimeAño(request):
    return render(request, 'appPE/busquedaAnimeAño.html')

def buscarAnimeAño(request):
    if request.GET['añoEstreno']:
        añoEstreno = request.GET['añoEstreno']
        animes = Anime.objects.filter(añoEstreno = añoEstreno)
        return render(request, 'appPE/resultadosAnimeAño.html', {'animes': animes, 'añoEstreno': añoEstreno})
    else:
        respuesta = "No se han ingresado datos"
    return HttpResponse(respuesta)
