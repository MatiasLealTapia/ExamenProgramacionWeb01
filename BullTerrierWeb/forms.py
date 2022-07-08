from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Carrito, Comentario, Producto, Suscripcion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['idComent', 'nombre', 'apellido', 'correo', 'calificacion', 'comentario']
        
class AddProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idPro', 'nombrePro', 'precioPro', 'descripPro', 'cantidadPro', 'mostrarPro', 'idCat' , 'imgPro']
        
class CustomUserCreationForm(UserCreationForm):
    pass

class SuscribirseForm(ModelForm):
    class Meta:
        model = Suscripcion
        fields = ['usu','donacion','suscrito']
        
class CarritoForm(ModelForm):
    class Meta:
        model = Carrito
        fields = ['idCarrito','cantidad','idPro','usuario']