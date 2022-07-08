from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import carrito, comentario, home, pedidos, productocompra, buscarProducto, productosgato, productoshamster, productosperro, registro, suscribirse, addProducto, listaProducto, comentariosLista, editarProducto, removeProducto, register, politicaDePrivacidad, detalle_suscritos, suscritos, lista_suscritos, agregarAlCarrito, carritoComprado, ProductoViewSet, CategoriaViewSet, SuscritosViewSet
from .viewlogin import login_user
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('categoria', CategoriaViewSet)
# router.register('suscritos', SuscritosViewSet)

urlpatterns = [
    #Index
    path('', home, name="index"),
    #Carrito
    path('carrito/', carrito, name="carrito"),
    #Carrito Comprado
    path('carrito/comprado/<id>/', carritoComprado, name="carritoComprado"),
    #Comentario
    path('comentario/', comentario, name="comentario"),
    #Comentarios tabla
    path('comentariosLista/', comentariosLista, name="comentariosLista"),
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
    path('productos/addCarrito/<id>/', agregarAlCarrito, name="agregarAlCarrito"),
    #Registrar usuario
    path('register/', register, name="register"),
    path('politica-de-privacidad/', politicaDePrivacidad, name="politicaDePrivacidad"),
    #-API-
    path('api/', include(router.urls)),
    path('login_user/', login_user, name='login_user'),
    path('suscritos/', suscritos, name='suscritos'),
    path('suscritos/lista', lista_suscritos, name='lista_suscritos'),
    path('detalle_suscritos/<id>', detalle_suscritos, name='detalle_suscritos'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
