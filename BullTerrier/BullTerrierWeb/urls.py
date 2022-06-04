from django.urls import path
from .views import carrito, comentario, home, pedidos, productocompra, productosgato, productoshamster, productosperro, registro, suscribirse

urlpatterns = [
    #Carrito
    path('carrito', carrito, name="carrito"),
    path('comentario', comentario, name="comentario"),
    path('', home, name="index"),
    path('pedidos', pedidos, name="pedidos"),
    path('productocompra', productocompra, name="productocompra"),
    path('productosgato', productosgato, name="productosgato"),
    path('productoshamster', productoshamster, name="productoshamster"),
    path('productosperro', productosperro, name="productosperro"),
    path('registro', registro, name="registro"),
    path('suscribirse', suscribirse, name="suscribirse"),
]
