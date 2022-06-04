from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def inicio(self):
    plantilla = loader.get_template('AppPE/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)
