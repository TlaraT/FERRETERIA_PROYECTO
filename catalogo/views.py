# catalogo/views.py
from django.shortcuts import render
from .models import Producto, Categoria

def inicio(request):
    productos_destacados = Producto.objects.filter(es_mas_vendido=True)
    context = {
        'productos': productos_destacados
    }
    return render(request, 'inicio.html', context)

def catalogo(request):
    categorias = Categoria.objects.all()
    categoria_seleccionada_id = request.GET.get('categoria')

    if categoria_seleccionada_id:
        productos = Producto.objects.filter(categoria_id=categoria_seleccionada_id)
    else:
        productos = Producto.objects.all()

    context = {
        'categorias': categorias,
        'productos': productos
    }
    return render(request, 'catalogo.html', context)

def quienes_somos(request):
    return render(request, 'quienes_somos.html')