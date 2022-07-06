from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import carrito, comentario, home, pedidos, productocompra, buscarProducto, productosgato, productoshamster, productosperro, registro, suscribirse, addProducto, listaProducto, comentariosLista, editarProducto, removeProducto, register, ProductoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)

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
    path('productos/producto/<id>/', productocompra, name="productocompra"),
    #Producto busqueda
    path('productos/', buscarProducto, name="buscarProducto"),
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
    #Editar producto
    path('productos/editar/<id>/', editarProducto, name="editarProducto"),
    #Eliminar producto
    path('productos/remove/<id>/', removeProducto, name="removeProducto"),
    #Registrar usuario
    path('register/', register, name="register"),
    # path('politica-de-privacidad/', politicaDePrivacidad, name="politicaDePrivacidad"),
    #-API-
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
