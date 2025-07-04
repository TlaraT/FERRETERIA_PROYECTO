# catalogo/models.py
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    imagen = models.ImageField(upload_to='productos_imagenes/')
    stock = models.PositiveIntegerField(default=0)
    es_mas_vendido = models.BooleanField(default=False, help_text="Marcar para que aparezca en la página de inicio")

    def __str__(self):
        return self.nombre