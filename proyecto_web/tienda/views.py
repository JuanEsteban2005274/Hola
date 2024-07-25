from django.shortcuts import render
from tienda.models import Producto

def tienda(request):
    product = Producto.objects.all()
    return render(request, 'tienda.html', {'productos': product})

def reporte(request):
    product = Producto.objects.all()
    return render(request, 'listado.html', {'productos': product})

def listado(request):
    product = Producto.objects.all()
    return render(request, 'listado.html', {'productos': product})
