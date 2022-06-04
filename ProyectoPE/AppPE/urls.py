from django.contrib import admin
from django.urls import path
# from AppPE import views
from AppPE.views import inicio, series, peliculas, libros, animes, mangas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='Inicio'),
    path('series/', series, name = 'Series'),
    path('peliculas/', peliculas, name = 'Peliculas'),
    path('libros/', libros, name = 'Libros'),
    path('animes/', animes, name = 'Animes'),
    path('mangas/', mangas, name = 'Mangas'),

]
