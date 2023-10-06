from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render
from .forms import CursoFormulario,





def saludo (request):
    return HttpResponse("hello")

def inicio(request):
    return render(request, "Appentrega/inicio.html")

def pag1(request):
    return render (request, "Appentrega/pag1.html")
def pag2(request):
    return render (request, "Appentrega/pag2.html")
def pag3(request):
    return render (request, "Appentrega/pag3.html")

def CursoFormulario(request):

    if request.method == 'POST':
        curso = Curso(nombre=request.POST['curso'],
                      camada=request.POST['camada'])
        curso.save()

        return render(request, "Appentrega/inicio.html")

    return render(request, "Appentrega/curseFormulario.html")


        