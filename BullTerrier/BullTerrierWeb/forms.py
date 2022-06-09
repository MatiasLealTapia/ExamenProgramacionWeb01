from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Comentario

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['idComent', 'nombre', 'apellido', 'correo', 'calificacion', 'comentario']