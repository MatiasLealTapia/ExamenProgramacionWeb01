from distutils.command.upload import upload
from django.db import models
import datetime
import os
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    idUsu = models.IntegerField(primary_key=True, verbose_name="Id Usuario")
    nombreUsu = models.CharField(max_length=50, verbose_name="Nombre de Usuario")
    emailUsu = models.CharField(max_length=50, verbose_name="Email")

    def __str__(self):
        return self.nombreUsu
    
class Categoria(models.Model):
    idCat = models.IntegerField(primary_key=True, verbose_name="Id Categoria")
    nomCat = models.CharField(max_length=30, verbose_name="Nombre Categoria")

    def __str__(self):
        return self.nomCat

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Producto(models.Model):
    idPro = models.IntegerField(primary_key=True, verbose_name="Id Producto") 
    nombrePro = models.CharField(max_length=100, verbose_name="Nombre Producto")
    precioPro = models.IntegerField(verbose_name="Precio Producto")
    descripPro = models.CharField(max_length=500, default="" ,verbose_name="Descripción")
    idCat = models.ForeignKey(Categoria, on_delete=models.CASCADE, default="0", verbose_name="Categoría")
    imgPro = models.ImageField(upload_to="productos", null=True, blank=True, verbose_name="Imagen")
    
    def __str__(self):
        return self.nombrePro

class Compra(models.Model):
    idCom = models.IntegerField(primary_key=True, verbose_name="Id Compra")
    fechaCom = models.DateField(verbose_name="Fecha Compra")
    descCom = models.CharField(max_length=1000, verbose_name="Descripción compra", default="")
    idPro = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Id Producto", default="0")
    idUsu = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Id Usuario", default="0")

    def __str__(self):
        return self.descCom

class Pedido(models.Model):
    idPed = models.IntegerField(primary_key=True, verbose_name="Id Pedido")
    descPed = models.CharField(max_length=1000, verbose_name="Descripción pedido", default="")
    idPro = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Id Producto", default="0")
    idUsu = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Id Usuario", default="0")

    def __str__(self):
        return self.descPed

class Comentario(models.Model):
    idComent = models.AutoField(primary_key=True, verbose_name="Id")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    correo = models.CharField(max_length=100, verbose_name="Correo electronico")
    calificacion = models.IntegerField(verbose_name="Calificación", default="0")
    comentario = models.CharField(max_length=500, null=True, verbose_name="Comentario")
    def __str__(self):
        return self.correo
    
class Suscripcion(models.Model):
    usu = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name="Usuario")
    suscrito = models.BooleanField(default='False')
    
    def __str__(self):
        return self.usu.username