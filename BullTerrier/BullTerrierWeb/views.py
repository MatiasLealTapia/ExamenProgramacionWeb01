from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'BullTerrierWeb/index.html')

def productosgato(request):
    return render(request, 'BullTerrierWeb/productosgato.html')

def productosperro(request):
    return render(request, 'BullTerrierWeb/productosperro.html')

def productoshamster(request):
    return render(request, 'BullTerrierWeb/productoshamster.html')

def productocompra(request):
    return render(request, 'BullTerrierWeb/productocompra.html')

def pedidos(request):
    return render(request, 'BullTerrierWeb/pedidos.html')

def carrito(request):
    return render(request, 'BullTerrierWeb/carrito.html')

def registro(request):
    return render(request, 'BullTerrierWeb/registro.html')