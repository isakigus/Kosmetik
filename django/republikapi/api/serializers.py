from rest_framework import serializers
from api import models


class AtributoCosmeticoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AtributoCosmetico
        fields = ('__all__')


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Producto
        fields = ('__all__')


class IngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ingrediente
        fields = ('__all__')


class ImagenSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Imagen
        fields = ('__all__')


class IngredienteRecetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.IngredienteReceta
        fields = ('__all__')


class RecetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Receta
        fields = ('__all__')


class PrecioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Precio
        fields = ('__all__')


class SearchInputSerializer(serializers.Serializer):
    search_text = serializers.CharField(max_length=250)
    search_mode = serializers.CharField(max_length=3, min_length=3)
