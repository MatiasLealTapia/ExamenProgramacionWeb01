from multiprocessing.spawn import import_main_path
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ComentarioForm, AddProductoForm, CustomUserCreationForm, SuscribirseForm, CarritoForm
from .models import Comentario, Categoria, Producto, Suscripcion, Carrito
from django.contrib import messages
from os import remove
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from .serializers import ProductoSerializer, CategoriaSerializer, SuscripcionSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class SuscritosViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer

# Vista Carrito
def carrito(request):
    usuario = request.user
    suscrito = False
    if usuario.is_authenticated:
        try:
            usuarioSuscrito = get_object_or_404(Suscripcion, usu=usuario)
            suscrito = False
            if usuarioSuscrito.suscrito:
                suscrito = True
            else:
                suscrito = False
        except:
            suscrito = False
    if usuario.is_authenticated:
        vacio = True
        try:
            comprasProductos = Carrito.objects.filter(usuario=usuario.id)
            if len(comprasProductos)!=0:
                vacio = False
                data = {
                    'vacio':vacio,
                    'productos':comprasProductos,
                    'idUsuario':usuario.id,
                    'suscrito':suscrito
                }
            else:
                vacio = True
                data = {
                    'vacio':vacio,
                    'suscrito':suscrito
                }
        except:
            data = {
                'vacio':vacio,
                'suscrito':suscrito
            }
    else:
        data = {
            'vacio': True,
            'suscrito':suscrito
        }
    return render(request, 'BullTerrierWeb/carrito.html', data)

def carritoComprado(request, id):
    productos = Carrito.objects.filter(usuario=id)
    for prod in productos:
        prod.delete()
    messages.success(request, "Comprado correctamente, muchas gracias por confiar en nosotros.")
    return redirect(to="carrito")

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
@login_required
def productocompra(request, id):
    usuario = request.user
    producto = get_object_or_404(Producto, idPro=id)
    
    data = {
        'prod':producto
    }
    
    if request.method=='POST':
        carritoNuevo = CarritoForm(request.POST)
        print(carritoNuevo)
        if carritoNuevo.is_valid():
            carritoNuevo.save()
            messages.success(request, "Agregado correctamente al carrito")
        return redirect(to="index")
    return render(request, 'BullTerrierWeb/producto/productocompra.html', data)

@login_required
def agregarAlCarrito(request, id):
    # producto = get_object_or_404(Producto, idPro=id)
    # productoId = int(producto.idPro)
    # usuario = request.user
    # agregarCarrito = CarritoForm()
    # agregarCarrito.idCarrito = 1
    # agregarCarrito.cantidad = 1
    # agregarCarrito.idPro = productoId
    # agregarCarrito.usuario = usuario.id
    # if agregarCarrito.is_valid():
    #     agregarCarrito.save()
    # agregarCarrito = Carrito.objects.create(idCarrito=1, cantidad=1, idPro=productoId, usuario=usuario.id)
    
    return redirect('/productos/producto/'+id+'/')

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
    productos = Producto.objects.all().filter(idCat=2)
    data = {
        'productos':productos
    }
    return render(request, 'BullTerrierWeb/producto/productosperro.html', data)

# Vista Registro
def registro(request):
    return render(request, 'BullTerrierWeb/registration/registro.html')

# Vista Suscribirse
def suscribirse(request):
    usuario = request.user
    if usuario.is_authenticated:
        try:
            usuarioSuscrito = get_object_or_404(Suscripcion, usu=usuario)
            suscrito = False
            if usuarioSuscrito.suscrito:
                suscrito = True
                data = {
                    'suscrito':suscrito
                }
            else:
                data = {
                    'suscrito':suscrito
                }
        except:
            data = {
                'noIdentificado':True,
                'suscrito':False
            }
    else:
        data = {
            
        }
    if request.method=='POST':
        suscribirNuevo = SuscribirseForm(data=request.POST, instance=usuarioSuscrito)
        print(suscribirNuevo)
        if suscribirNuevo.is_valid():
            suscribirNuevo.save()
            messages.success(request, "Muchas gracias por tu donacion, disfruta de tus descuentos")
        return redirect(to="index")
    
    return render(request, 'BullTerrierWeb/suscribirse.html', data)

# Base (header y footer)
def base(request):
    return render(request, 'BullTerrierWeb/base.html')

# Busqueda de producto
def buscarProducto(request):
    data={
        'productos':Producto.objects.all()
    }
    queryset = request.GET.get("search")
    print(queryset)
    if queryset:
        productos = Producto.objects.filter(
            Q(nombrePro__icontains = queryset) |
            Q(descripPro__icontains = queryset)
        ).distinct()
        print(productos)
        data={
            'productos':productos
        }
    elif queryset == "":
        productos = Producto.objects.all()
        data={
            'productos':productos
        }
    return render(request, 'BullTerrierWeb/producto/buscar.html', data)

# Vista Añadir producto
@permission_required('BullTerrierWeb.add_producto')
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
            producto.cantidadPro = request.POST.get("id_cantidadPro")
            producto.mostrarPro = request.POST.get("id_mostrarPro")
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
@permission_required('BullTerrierWeb.change_producto')
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
@permission_required('BullTerrierWeb.delete_producto')
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

def politicaDePrivacidad(request):
    return render(request, 'BullTerrierWeb/politica-de-privacidad.html')

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def suscritos(request):
    if request.method=='GET':
        suscripcion = Suscripcion.objects.all() #<=> SELECT * FROM Producto
        serializer = SuscripcionSerializer(suscripcion, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = SuscripcionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_suscritos(request, id):
    try:
        donacion = Suscripcion.objects.get(id=id)
    except Suscripcion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=SuscripcionSerializer(donacion)
        return Response(serializer.data)

    if request.method=='PUT': 
        data = JSONParser().parse(request)
        serializer = SuscripcionSerializer(donacion, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method=='DELETE':
        donacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@login_required
def lista_suscritos(request):

    url = "http://127.0.0.1:8000/suscritos"
    token = Token.objects.get(user=request.user)
    headers = {'Authorization': f'Token {token}'}

    suscripciones = request.get(url, headers=headers).json()

    data = {
        'suscripciones' : suscripciones,
    }

    return render(request, 'suscritos/lista.html', data)