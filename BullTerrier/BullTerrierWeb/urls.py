from django.urls import path
from .views import carrito, comentario, home, pedidos, productocompra, productosgato, productoshamster, productosperro, registro, suscribirse, envio

urlpatterns = [
    #Carrito
    path('carrito', carrito, name="carrito"),
    #Comentario
    path('comentario', comentario, name="comentario"),
    #Index
    path('', home, name="index"),
    #Pedidos
    path('pedidos', pedidos, name="pedidos"),
    #Producto Compra
    path('productocompra', productocompra, name="productocompra"),
    #Productos gato
    path('productosgato', productosgato, name="productosgato"),
    #Productos Hamster
    path('productoshamster', productoshamster, name="productoshamster"),
    #Productos Perro
    path('productosperro', productosperro, name="productosperro"),
    #Registro
    path('registro', registro, name="registro"),
    #Suscribirse
    path('suscribirse', suscribirse, name="suscribirse"),
    #Envio
    path('envio', envio, name="envio"),
]
