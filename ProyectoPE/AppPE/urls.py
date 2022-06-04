from django.contrib import admin
from django.urls import path
# from AppPE import views
from AppPE.views import inicio, series, peliculas, libros, animes, mangas, serieFormulario, peliculaFormulario, libroFormulario, animeFormulario, mangaFormulario

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

]
