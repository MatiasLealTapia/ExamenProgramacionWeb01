from django.urls import path
from .views import home, productosgato, productosperro, productoshamster, productocompra

urlpatterns = [
    path('', home, name="index"),
    path('index.html', home, name="index"),
    path('productosgato.html', productosgato, name="productosgato"),
    path('productosperro.html', productosperro, name="productosperro"),
    path('productoshamster.html', productoshamster, name="productoshamster"),
    path('productocompra.html', productocompra, name="productocompra"),
]
