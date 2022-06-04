from django.urls import path
from .views import home, productosgato, productosperro, productoshamster, productocompra, pedidos, carrito, registro

urlpatterns = [
    path('', home, name="index"),
    path('productosgato', productosgato, name="productosgato"),
    path('productosperro', productosperro, name="productosperro"),
    path('productoshamster', productoshamster, name="productoshamster"),
    path('productocompra', productocompra, name="productocompra"),
    path('pedidos', pedidos, name="pedidos"),
    path('carrito', carrito, name="carrito"),
    path('registro', registro, name="registro"),
]
