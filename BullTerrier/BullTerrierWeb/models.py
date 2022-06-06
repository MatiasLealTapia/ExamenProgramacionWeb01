from operator import mod
from pyexpat import model
from django.db import models
# Create your models here.

class Usuario(models.Model):
    idUsu = models.IntegerField(primary_key=True, verbose_name="Id Usuario")
    nombreUsu = models.CharField(max_length=50, verbose_name="Nombre de Usuario")
    emailUsu = models.CharField(max_length=50, verbose_name="Email")

    def __str__(self):
        return self.nombreUsu

class Producto(models.Model):
    idPro = models.IntegerField(primary_key=True, verbose_name="Id Producto") 
    nombrePro = models.CharField(max_length=100, verbose_name="Nombre Producto")
    precioPro = models.IntegerField(verbose_name="Precio Producto")
    #idCat = models.IntegerField(primary_key=True, verbose_name="Id Categoria")

class Categoria(models.Model):
    idCat = models.IntegerField(primary_key=True, verbose_name="Id Categoria")
    nomCat = models.CharField(max_length=30, verbose_name="Nombre Categoria")

class Compra(models.Model):
    idCom = models.IntegerField(primary_key=True, verbose_name="Id Compra")
    fechaCom = models.DateField(verbose_name="Fecha Compra")
    #idPro = models.IntegerField(primary_key=True, verbose_name="Id Producto")
    #idUsu = models.IntegerField(primary_key=True, verbose_name="Id Usuario")

class Pedido(models.Model):
    idPed = models.IntegerField(primary_key=True, verbose_name="Id Pedido")
    #idPro = models.IntegerField(primary_key=True, verbose_name="Id Producto")
    #idUsu = models.IntegerField(primary_key=True, verbose_name="Id Usuario")