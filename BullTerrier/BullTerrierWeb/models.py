from django.db import models
# Create your models here.

class Usuario(models.Model):
    idUsu = models.IntegerField(primary_key=True, verbose_name="Id del Usuario")
    nombreUsu = models.CharField(max_length=50, verbose_name="Nombre de Usuario")

    def __str__(self):
        return self.nombreUsu