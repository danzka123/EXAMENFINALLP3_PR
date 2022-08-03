from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request,'inicio.html', {
        'titulo':'Inicio',
        'mensaje':'Mensaje Saludo',
    })
def integrantes(request):
    estudiantes = 'Kevin Arturo Pinedo Romero'
    return render(request,'integrantes.html', {
        'titulo':'Integrantes',
        'estudiante': estudiantes,
    })
def crearcursos(request):
    return render(request, 'crearcursos.html', {
    })

def crearproductos(request):
    return render(request, 'crearproductos.html', {
    })
