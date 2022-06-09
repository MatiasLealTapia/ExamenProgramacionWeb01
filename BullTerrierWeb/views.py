from django.shortcuts import render, redirect
from .forms import ComentarioForm, AddProductoForm, RemoveProductoForm
from .models import Comentario, Categoria, Producto

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
    if Producto.objects.all().count()==0:
        idProducto=1
    else:
        idProducto=Producto.objects.all().count()+1
    datos = {
        'idProducto':idProducto,
        'form': AddProductoForm(),
        'categorias': Categoria.objects.all()
    }
    if request.method == "POST":
        producto = AddProductoForm(request.POST, request.FILES)
        if producto.is_valid():
            producto.idPro = request.POST.get("id_idPro")
            producto.nombrePro = request.POST.get("id_nombrePro")
            producto.precioPro = request.POST.get("id_precioPro")
            producto.descripPro = request.POST.get("id_descripPro")
            producto.idCat = request.POST.get("id_idCat")
            producto.imgPro = request.FILES.get("id_imgPro")
        
            producto.save()
            mensaje={
                'envio': "Enviado"         
                }
            return render(request, 'BullTerrierWeb/envio.html', mensaje)
    return render(request, 'BullTerrierWeb/addProducto.html', datos)

# Vista Borrar Productos

def removeProducto(request):
    datos = {
        'productos':Producto.objects.all()
    }
    # if request.method == "POST":
    #     producto=RemoveProductoForm(request.POST)
    #     producto.idPro = request.POST.get("id_idPro")
    #     idPro = producto.idPro
    #     remover = Producto.objects.get(idPro=idPro)
    #     remover.delete()
    #     return redirect(to="removeProducto")
    return render(request, 'BullTerrierWeb/removeProducto.html', datos)

def comentariosLista(request):
    datos = {
        'comentarios':Comentario.objects.all()
    }
    return render(request, 'BullTerrierWeb/comentariosLista.html', datos)