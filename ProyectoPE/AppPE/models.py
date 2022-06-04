from django.db import models

class Serie(models.Model):
    nombre = models.CharField(max_length=40)
    temporadas = models.IntegerField()
    episodios = models.IntegerField()
    añoEstreno = models.IntegerField()
    director = models.CharField(max_length=40)

class Pelicula(models.Model):
    nombre = models.CharField(max_length=40)
    duracion = models.IntegerField()
    añoEstreno = models.IntegerField()
    director = models.CharField(max_length=40)

class Libro(models.Model):
    nombre =  models.CharField(max_length=40)
    añoPublicacion = models.IntegerField()
    paginas = models.IntegerField()
    autor = models.CharField(max_length=40)

class Anime(models.Model):
    nombre = models.CharField(max_length=40)
    temporadas = models.IntegerField()
    episodios = models.IntegerField()
    añoEstreno = models.IntegerField()
    director = models.CharField(max_length=40)

class Manga(models.Model):
    nombre = models.CharField(max_length=40)
    añoPublicacion = models.IntegerField()
    paginas = models.IntegerField()
    autor = models.CharField(max_length=40)


