from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Comentario, Producto

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['idComent', 'nombre', 'apellido', 'correo', 'calificacion', 'comentario']
        
class AddProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idPro', 'nombrePro', 'precioPro', 'descripPro', 'idCat' , 'imgPro']
        
class RemoveProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idPro']