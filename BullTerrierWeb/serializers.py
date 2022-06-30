from .models import Categoria, Producto
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    nomCat = serializers.CharField(read_only=True, source="idCat.nomCat")
    class Meta:
        model = Producto
        fields = '__all__'