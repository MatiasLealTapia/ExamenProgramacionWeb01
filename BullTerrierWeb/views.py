import imp
from multiprocessing.spawn import import_main_path
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ComentarioForm, AddProductoForm, CustomUserCreationForm
from .models import Comentario, Categoria, Producto
from django.contrib import messages
from os import remove
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login

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
            messages.success(request, "Comentario enviado correctamente")
            return redirect(to="index")
    return render(request, 'BullTerrierWeb/comentario.html', datos)

# Vista Index
def home(request):
    return render(request, 'BullTerrierWeb/index.html')

# Vista Pedidos
def pedidos(request):
    return render(request, 'BullTerrierWeb/pedidos.html')

# Vista Producto Compra
def productocompra(request):
    return render(request, 'BullTerrierWeb/producto/productocompra.html')

# Vista Productos Gato
def productosgato(request):
    productos = Producto.objects.all().filter(idCat=3)
    data = {
        'productos':productos
    }
    return render(request, 'BullTerrierWeb/producto/productosgato.html', data)

# Vista Productos Hamster
def productoshamster(request):
    return render(request, 'BullTerrierWeb/producto/productoshamster.html')

# Vista Productos Perro
def productosperro(request):
    return render(request, 'BullTerrierWeb/producto/productosperro.html')

# Vista Registro
def registro(request):
    return render(request, 'BullTerrierWeb/registration/registro.html')

# Vista Suscribirse
def suscribirse(request):
    return render(request, 'BullTerrierWeb/suscribirse.html')

# Base (header y footer)
def base(request):
    return render(request, 'BullTerrierWeb/base.html')

# Vista Añadir producto
def addProducto(request):
    if Producto.objects.all().count()==0:
        idProducto=1
    else:
        idProducto=Producto.objects.latest("idPro")
        idProducto=idProducto.idPro+1
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
            messages.success(request, "Producto agregado correctamente")
            return redirect(to="listaProducto")
    return render(request, 'BullTerrierWeb/producto/addProducto.html', datos)

# Vista Borrar Productos
def listaProducto(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    
    datos = {
        'entity':productos,
        'paginator':paginator
    }
    return render(request, 'BullTerrierWeb/producto/lista.html', datos)

# Vista Lista Comentarios
def comentariosLista(request):
    comentarios = Comentario.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(comentarios, 5)
        comentarios = paginator.page(page)
    except:
        raise Http404
    
    datos = {
        'entity':comentarios,
        'paginator':paginator
    }
    return render(request, 'BullTerrierWeb/comentariosLista.html', datos)

# Vista Editar Producto
def editarProducto(request, id):
    
    producto = get_object_or_404(Producto, idPro=id)
    
    data = {
        'form': AddProductoForm(instance=producto),
        'prod':producto,
        'idCate':str(producto.idCat),
        'categorias': Categoria.objects.all()
    }
    
    if request.method == 'POST':
        formulario = AddProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Editado correctamente")
            return redirect(to="listaProducto")
        data["form"] = formulario
        
    return render(request, 'BullTerrierWeb/producto/editar.html', data)

# Eliminar Producto
def removeProducto(request, id):
    producto = get_object_or_404(Producto, idPro=id)
    if producto.imgPro:
        urlImg = producto.imgPro.path
        remove(urlImg)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listaProducto")

# Registrar Usuario
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='index')
        data["form"] = formulario
    
    return render(request, 'BullTerrierWeb/register.html', data)
