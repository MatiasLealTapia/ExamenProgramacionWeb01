from django.shortcuts import render

# Create your views here.

# Vista Carrito
def carrito(request):
    return render(request, 'BullTerrierWeb/carrito.html')

# Vista Comentario
def comentario(request):
    return render(request, 'BullTerrierWeb/comentario.html')

# Vista Index
def home(request):
    return render(request, 'BullTerrierWeb/index.html')

# Vista Pedidos
def pedidos(request):
    return render(request, 'BullTerrierWeb/pedidos.html')

# Vista Producto Compra
def productocompra(request):
    return render(request, 'BullTerrierWeb/productocompra.html')

# Vista Productos Gato
def productosgato(request):
    return render(request, 'BullTerrierWeb/productosgato.html')

# Vista Productos Hamster
def productoshamster(request):
    return render(request, 'BullTerrierWeb/productoshamster.html')

# Vista Productos Perro
def productosperro(request):
    return render(request, 'BullTerrierWeb/productosperro.html')

# Vista Registro
def registro(request):
    return render(request, 'BullTerrierWeb/registro.html')

# Vista Suscribirse
def suscribirse(request):
    return render(request, 'BullTerrierWeb/suscribirse.html')