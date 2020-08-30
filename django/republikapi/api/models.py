from django.db import models
from enum import Enum


class CategoriaImagen(Enum):
    imagen = "imagen"
    etiqueta = "etiqueta"


class AtributoCosmetico(models.Model):
    value = models.TextField()

    def __str__(self):
        return f"{self.value}"


class Tienda(models.Model):
    value = models.TextField()

    def __str__(self):
        return f"{self.value}"


class CategoriaIngrediente(models.Model):
    value = models.TextField()

    def __str__(self):
        return f"{self.value}"


class CategoriaCosmetica(models.Model):
    value = models.TextField()

    def __str__(self):
        return f"{self.value}"


class Producto(models.Model):
    nombre = models.TextField()
    comentario = models.TextField(default='')
    propiedades = models.ManyToManyField(AtributoCosmetico, blank=True)
    categoria = models.ForeignKey(
        CategoriaCosmetica, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}, {self.categoria}"


class Ingrediente(models.Model):
    nombre = models.TextField()
    comentario = models.TextField(default='')
    propiedades = models.ManyToManyField(AtributoCosmetico, blank=True)
    categoria = models.ForeignKey(
        CategoriaIngrediente, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}, {self.categoria}"


class Imagen(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to='images')
    categoria = models.TextField(
        choices=[(item.value, item.name) for item in CategoriaImagen]
    )

    def __str__(self):
        return f"{self.producto.nombre}, {self.categoria}"


class IngredienteReceta(models.Model):
    ingrediente = models.ForeignKey(
        Ingrediente, on_delete=models.SET_NULL, null=True)
    porcentaje = models.DecimalField(decimal_places=4, max_digits=8)

    def __str__(self):
        return f"{self.ingrediente.nombre}, {self.porcentaje}"


class Receta(models.Model):
    ingredientes = models.ManyToManyField(IngredienteReceta)
    producto = models.ForeignKey(
        Producto, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Receta #{self.id} de {self.producto.nombre}"


class Precio(models.Model):
    ingrediente = models.ForeignKey(
        Ingrediente, on_delete=models.SET_NULL, null=True)
    tienda = models.ForeignKey(
        Tienda, on_delete=models.SET_NULL, null=True)
    fecha_compra = models.DateTimeField()
    value = models.DecimalField(decimal_places=2, max_digits=8)
    currency = models.TextField(default="EUR")

    def __str__(self):
        return f"{self.ingrediente.nombre}, {self.tienda}, {self.value} {self.currency} [{self.fecha_compra}]"
