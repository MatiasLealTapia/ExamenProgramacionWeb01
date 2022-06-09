from django.shortcuts import render, redirect
from .forms import ComentarioForm
from .models import Comentario

# Create your views here.

# Vista Carrito
def carrito(request):
    return render(request, 'BullTerrierWeb/carrito.html')

# Vista Comentario
def comentario(request):
    datos = {
        'form': ComentarioForm()
    }
    
    if request.method=='POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()            
            mensaje={
                'envio': "Enviado"         
            }
        return render(request, 'BullTerrierWeb/envio.html', mensaje)
    return render(request, 'BullTerrierWeb/comentario.html', datos)

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

# Vista Envio
def envio(request):
    mensaje={
        'envio': "Mensaje invalido"         
    }
    return render(request, 'BullTerrierWeb/envio.html', mensaje)

# Vista Base (header y footer)
def base(request):
    return render(request, 'BullTerrierWeb/base.html')

# Vista Añadir producto

def addProducto(request):
    return render(request, 'BullTerrierWeb/addProducto.html')