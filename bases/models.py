from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    #Fecha de creación
    #Solo cuando el objeto se cree
    fc = models.DateTimeField(auto_now_add=True)
    #Fecha modificado
    fm = models.DateTimeField(auto_now=True)
    #Usuario que crea
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    #Con esto no toma en cuenta el modelo al crear la
    #migración
    class Meta:
        abstract=True
