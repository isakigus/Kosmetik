
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api import models
from api import serializers
from api import repo


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = models.Producto.objects.all()
    serializer_class = serializers.ProductoSerializer


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = models.Ingrediente.objects.all()
    serializer_class = serializers.IngredienteSerializer


class ImagenViewSet(viewsets.ModelViewSet):
    queryset = models.Imagen.objects.all()
    serializer_class = serializers.ImagenSerializer


class IngredienteRecetaViewSet(viewsets.ModelViewSet):
    queryset = models.IngredienteReceta.objects.all()
    serializer_class = serializers.IngredienteRecetaSerializer


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = models.Receta.objects.all()
    serializer_class = serializers.RecetaSerializer


class PrecioViewSet(viewsets.ModelViewSet):
    queryset = models.Precio.objects.all()
    serializer_class = serializers.PrecioSerializer


class AtributoCosmeticoViewSet(viewsets.ModelViewSet):
    queryset = models.AtributoCosmetico.objects.all()
    serializer_class = serializers.AtributoCosmeticoSerializer



class SearchList(APIView):
    def post(self, request, format=None):
        serializer = serializers.SearchInputSerializer(data=request.data)
        if serializer.is_valid():
            result_list = repo.find_search_results(serializer.data)
            return Response(result_list, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
