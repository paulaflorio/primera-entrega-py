from django import forms

class SerieFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    temporadas = forms.IntegerField()
    episodios = forms.IntegerField()
    añoEstreno = forms.IntegerField()
    director = forms.CharField(max_length=40)

class PeliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    duracion = forms.IntegerField()
    añoEstreno = forms.IntegerField()
    director = forms.CharField(max_length=40)

class LibroFormulario(forms.Form):
    nombre =  forms.CharField(max_length=40)
    añoPublicacion = forms.IntegerField()
    paginas = forms.IntegerField()
    autor = forms.CharField(max_length=40)

class AnimeFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    temporadas = forms.IntegerField()
    episodios = forms.IntegerField()
    añoEstreno = forms.IntegerField()
    director = forms.CharField(max_length=40)

class MangaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    añoPublicacion = forms.IntegerField()
    paginas = forms.IntegerField()
    autor = forms.CharField(max_length=40)
