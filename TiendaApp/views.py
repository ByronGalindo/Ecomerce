from django.shortcuts import render
from .models import CategoriaProdcuto, Producto


# Create your views here.

def tienda(request):
    
    Productos = Producto.objects.all()
    return render(request, 'TiendaApp/tienda.html',{"Productos":Productos})