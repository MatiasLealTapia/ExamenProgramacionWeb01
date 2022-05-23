from django.urls import path
from .views import home, productosgato, productosperro, productoshamster

urlpatterns = [
    path('', home, name="index"),
    path('productosgato.html', productosgato, name="productosgato"),
    path('', productosperro, name="productosperro"),
    path('', productoshamster, name="productoshamster"),
]
