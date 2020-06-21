from django.db import models
from bases.models import ClaseModelo

# Create your models here.

class CategoriaModelo(ClaseModelo):
    descripcion = models.TextField(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper(),
        super(CategoriaModelo, self).save()

    class Meta:
        verbose_name_plural = "Categorias"

class SubCategoriaModel(ClaseModelo):
    categoria = models.ForeignKey(CategoriaModelo, on_delete=models.CASCADE)
    descripcion = models.TextField(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoriaModel, self).save()

    class Meta:
        verbose_name_plural = "SubCategorias"
        unique_together = ('categoria', 'descripcion')


