from django.db import models

class Universidad(models.Model):
    edificio1 = models.CharField(max_length=100)
    edificio2 = models.CharField(max_length=100)
    edificio3 = models.CharField(max_length=100)
    edificio4 = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.edificio1
