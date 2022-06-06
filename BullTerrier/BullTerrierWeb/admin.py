from django.contrib import admin
from .models import Categoria, Compra, Usuario, Producto, Pedido

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(Pedido)
admin.site.register(Categoria)