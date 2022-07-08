from csv import list_dialects
from django.contrib import admin
from .models import Categoria, Comentario, Compra, Usuario, Producto, Pedido, Suscripcion, Carrito

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["idPro","nombrePro","precioPro","idCat","descripPro","imgPro"]
    list_editable = ["nombrePro","precioPro","descripPro"]
    list_filter = ["idCat"]
    search_fields = ["nombrePro"]
    list_per_page = 10
    
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ["idComent","nombre","apellido","correo","calificacion","comentario"]
    list_per_page = 20
    
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ["nomCat","idCat"]
    
class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ["usu","suscrito"]

admin.site.register(Usuario)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Compra)
admin.site.register(Pedido)
admin.site.register(Carrito)
admin.site.register(Categoria, CategoriasAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Suscripcion, SuscripcionAdmin)