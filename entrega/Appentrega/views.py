from django.http import HttpResponse
from django.template import Template, context
from django.template import loader
from django.shortcuts import render
from .models import Curso
from .forms import CursoFormulario, BuscaCursoForm




def saludo (request):
    return HttpResponse("hello")

def inicio(request):
    return render(request, "Appentrega/inicio.html")

def curso(request):
    pass
def pag1(request):
    return render (request, "Appentrega/pag1.html")
def pag2(request):
    return render (request, "Appentrega/pag2.html")
def pag3(request):
    return render (request, "Appentrega/pag3.html")


def cursoFormulario(request):

    if request.method == 'POST':
        curso = Curso(nombre= request.POST ['curso'],
                      camada=request.POST['camada'])
        curso.save()

        return render(request, "Appentrega/inicio.html")

    return render(request, "Appentrega/cursoFormulario.html")

def buscarCurso(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = BuscaCursoForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            cursos = Curso.objects.filter(
                nombre__icontains=informacion["curso"])

            return render(request, "Appentrega/lista.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "Appentrega/buscarCurso.html", {"miFormulario": miFormulario})


def mostrar(request):

    pass

def read_cursos(request):

    cursos = Curso.objects.all()  # trae todos los cursos

    contexto = {"cursos": cursos}

    return render(request, "Appentrega/readcurso.html", contexto)


def edit_curso(request, curso_id):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            curso = Curso.objects.get(id=curso_id)
            curso.nombre = informacion["curso"]
            curso.camada = informacion["camada"]
            curso.save()

            return render(request, "Appentrega/inicio.html")
    else:
        curso = Curso.objects.get(id=curso_id)
        miFormulario = CursoFormulario(
            initial={"curso": curso.nombre, "camada": curso.camada})

    return render(request, "Appentrega/editCursos.html", {"miFormulario": miFormulario})


def delete_curso(request, curso_id):

    curso = Curso.objects.get(id=int(curso_id))
    curso.delete()

    # vuelvo al menú
    cursos = Curso.objects.all()  # trae todos los cursos
    return render(request, "Appentrega/readcurso.html", {"cursos": cursos})

def detalle_curso(request, curso_id):

    curso = Curso.objects.get(id=int(curso_id))
    return render(request, 'Appentrega/ver_curso.html', {'curso': curso})