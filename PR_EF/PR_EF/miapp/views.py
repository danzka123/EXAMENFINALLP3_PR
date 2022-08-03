from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Producto

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
        precio_venta = "7 Soles",
        fecha_compra = "2022-07-25",
        fecha_registro = "2022-08-02",
        estado = "A"   
    )
    producto.save()
    return HttpResponse(f"Producto creado: {producto.codigo} - {producto.nombre} - {producto.precio_compra} - {producto.precio_venta} - {producto.fecha_compra} - {producto.fecha_registro} - {producto.estado}")