"""Categoria 

    Responsável pelo serviço do cardapio 
    Gabriel Rodrigues dos Santos
    01/04/2025
"""
from restaurante.models.categoria import Categoria
from restaurante.models.cardapio import Cardapio
from restaurante.serializers import CategoriaSerializer, CardapioSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status

class CategoriaServices(ViewSet):
    
    def list(self, request):
        categoria = Categoria.objects
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)
        
    
    def update(self, request, pk=None):
        categoria = get_object_or_404(Categoria, pk=pk)
        
        serializer = CategoriaSerializer(categoria, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return Response(status = status.HTTP_200_OK)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request):
        categoria = CategoriaSerializer(data=request.data)
        if categoria.is_valid():
            categoria.save()
            return Response(categoria.data, status=status.HTTP_200_OK)
        
        return Response(categoria.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=["get"], url_path="itens-associados" )
    def itens_associados(self, request, pk=None):
        """Retorna os itens do cardápio associados a uma determinada categoria.
        Ex: http://127.0.0.1:8000/api/categoria/2/itens-associados/
        """
        categoria = get_object_or_404(Categoria, pk=pk)
        itens = Cardapio.objects.filter(cat_id=categoria)  # Filtra os itens da categoria
        
        serializer = CardapioSerializer(itens, many=True)  # Serializa a lista de itens
        return Response(serializer.data)