from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages

# Create your views here.

def home(request):
    cursos1 = Curso.objects.all()
    messages.success(request, '!Cursos Listados!')
    return render(request, "gestionCursos.html", {"cursos": cursos1})
    
def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '!Cursos registrado!')
    return redirect('/')

def edicionCurso(request, codigo):
    curso= Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso= Curso.objects.get(codigo=codigo)
    curso.nombre= nombre
    curso.creditos= creditos
    curso.save()
    messages.success(request, '!Curso Actualizado!')
    return redirect('/')


def eliminacionCurso(request, codigo):
    curso= Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, '!Cursos Eliminado!')
    return redirect('/')