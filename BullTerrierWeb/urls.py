from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import carrito, comentario, home, pedidos, productocompra, productosgato, productoshamster, productosperro, registro, suscribirse, addProducto, listaProducto, comentariosLista, editarProducto, removeProducto, register

urlpatterns = [
    #Carrito
    path('carrito/', carrito, name="carrito"),
    #Comentario
    path('comentario/', comentario, name="comentario"),
    #Comentarios tabla
    path('comentariosLista/', comentariosLista, name="comentariosLista"),
    #Index
    path('', home, name="index"),
    #Pedidos
    path('pedidos/', pedidos, name="pedidos"),
    #Producto Compra
    path('productos/producto/', productocompra, name="productocompra"),
    #Productos gato
    path('productos/gato/', productosgato, name="productosgato"),
    #Productos Hamster
    path('productos/hamster/', productoshamster, name="productoshamster"),
    #Productos Perro
    path('productos/perro/', productosperro, name="productosperro"),
    #Registro
    path('registro/', registro, name="registro"),
    #Suscribirse
    path('suscribirse/', suscribirse, name="suscribirse"),
    #Añadir producto
    path('productos/add/', addProducto, name="addProducto"),
    #Listar productos
    path('productos/lista/', listaProducto, name="listaProducto"),
    #Editr producto
    path('productos/editar/<id>/', editarProducto, name="editarProducto"),
    path('productos/remove/<id>/', removeProducto, name="removeProducto"),
    path('register/', register, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
