from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Producto
from miapp.models import Curso

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
def crearproducto1(request):
    producto=Producto(
        codigo= "DL213",
        nombre= "Queso",
        precio_compra = "5 Soles",
        precio_venta = "70 Soles",
        fecha_compra = "2022-07-25",
        fecha_registro = "2022-08-02",
        estado = "B"   
    )
    producto.save()
    return HttpResponse(f"Producto creado: {producto.codigo} - {producto.nombre} - {producto.precio_compra} - {producto.precio_venta} - {producto.fecha_compra} - {producto.fecha_registro} - {producto.estado}")
def crearcurso1(request):
    curso=Curso(
        codigo= "SD005",
        nombre = "Estadistica",
        horas= "4 Horas",
        creditos = "4",
        fecha_registro = "2021-02-02",
        estado = "A"   
    )
    curso.save()
    return HttpResponse(f"Producto creado: {curso.codigo} - {curso.nombre} - {curso.horas} - {curso.creditos} - {curso.fecha_registro} - {curso.estado}")