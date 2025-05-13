from django.db import models

# Create your models here.
class Comida(models.Model):
    nombre = models.CharField(max_length=100)
    ingrediente_principal = models.CharField(max_length=100)
    calorias = models.IntegerField()
    peso = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre 