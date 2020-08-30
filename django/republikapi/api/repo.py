from api import models
from api import serializers


def find_search_results(data):
    search_mode = data.get('search_mode')
    text = data.get('search_text')
    ingredientes = []
    productos = []

    if search_mode in ['ING', 'ALL']:
        ingredientes_queryset = models.Ingrediente.objects.filter(nombre__contains=text)
        ingredientes = serializers.IngredienteSerializer(ingredientes_queryset, many=True).data

    if search_mode in ['PRO', 'ALL']:
        productos_queryset = models.Producto.objects.filter(nombre__contains=text)
        productos = serializers.ProductoSerializer(productos_queryset, many=True).data

    return productos + ingredientes
