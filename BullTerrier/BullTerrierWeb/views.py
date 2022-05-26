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