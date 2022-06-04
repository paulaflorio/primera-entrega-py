from django.contrib import admin
from django.urls import path
# from AppPE import views
from AppPE.views import inicio, series, peliculas, libros, animes, mangas, serieFormulario, peliculaFormulario, libroFormulario, animeFormulario, mangaFormulario, busquedaPeliculaDirector, buscarPeliculaDirector, busquedaPeliculaAño, buscarPeliculaAño, busquedaSerieDirector, buscarSerieDirector,busquedaSerieAño, buscarSerieAño, busquedaLibroAutor, buscarLibroAutor, busquedaLibroAño, buscarLibroAño, busquedaMangaAutor, buscarMangaAutor, busquedaMangaAño, buscarMangaAño, busquedaAnimeDirector, busquedaAnimeAño, buscarAnimeDirector, buscarAnimeAño

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='Inicio'),
    path('series/', series, name = 'Series'),
    path('peliculas/', peliculas, name = 'Peliculas'),
    path('libros/', libros, name = 'Libros'),
    path('animes/', animes, name = 'Animes'),
    path('mangas/', mangas, name = 'Mangas'),
    path('serieFormulario/', serieFormulario, name='serieFormulario'),
    path('peliculaFormulario/', peliculaFormulario, name='peliculaFormulario'),
    path('libroFormulario/', libroFormulario, name='libroFormulario'),
    path('animeFormulario/', animeFormulario, name='animeFormulario'),
    path('mangaFormulario/', mangaFormulario, name='mangaFormulario'),
    path('busquedaPeliculaDirector/', busquedaPeliculaDirector, name = 'busquedaPeliculaDirector'),
    path('buscarPeliculaDirector/', buscarPeliculaDirector, name = 'buscarPeliculaDirector'),
    path('busquedaPeliculaAño/', busquedaPeliculaAño, name = 'busquedaPeliculaAño'),
    path('buscarPeliculaAño/', buscarPeliculaAño, name = 'buscarPeliculaAño'),
    path('busquedaSerieDirector/', busquedaSerieDirector, name = 'busquedaSerieDirector'),
    path('buscarSerieDirector/', buscarSerieDirector, name = 'buscarSerieDirector'),
    path('busquedaSerieAño/', busquedaSerieAño, name = 'busquedaSerieAño'),
    path('buscarSerieAño/', buscarSerieAño, name = 'buscarSerieAño'),
    path('busquedaLibroAutor/', busquedaLibroAutor, name = 'busquedaLibroAutor'),
    path('buscarLibroAutor/', buscarLibroAutor, name = 'buscarLibroAutor'),
    path('busquedaLibroAño/', busquedaLibroAño, name = 'busquedaLibroAño'),
    path('buscarLibroAño/', buscarLibroAño, name = 'buscarLibroAño'),
    path('busquedaMangaAutor/', busquedaMangaAutor, name = 'busquedaMangaAutor'),
    path('buscarMangaAutor/', buscarMangaAutor, name = 'buscarMangaAutor'),
    path('busquedaMangaAño/', busquedaMangaAño, name = 'busquedaMangaAño'),
    path('buscarMangaAño/', buscarMangaAño, name = 'buscarMangaAño'),
    path('busquedaAnimeDirector/', busquedaAnimeDirector, name = 'busquedaAnimeDirector'),
    path('buscarAnimeDirector/', buscarAnimeDirector, name = 'buscarAnimeDirector'),
    path('busquedaAnimeAño/', busquedaAnimeAño, name = 'busquedaAnimeAño'),
    path('buscarAnimeAño/', buscarAnimeAño, name = 'buscarAnimeAño'),

]
