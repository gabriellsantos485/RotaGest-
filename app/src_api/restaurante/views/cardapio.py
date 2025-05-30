"""
Cardapio ou menu do sistema 

Respnsável por devolver o cardapio com itens para o usuario
Gabriel Rodrigues dos Santos 
27/03/2025
"""

from restaurante.models.cardapio import Cardapio
from restaurante.serializers import CardapioSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status

class CardapioService(ViewSet):
    
    def list(self, request):
        # Busca todos os itens do cardápio, otimizando o acesso à categoria
        cardapio_items = Cardapio.objects.filter(car_status=1).select_related('cat_id')
        
        # Serializa os itens do cardápio
        serializer = CardapioSerializer(cardapio_items, many=True)  # many=True para serializar múltiplos itens
        
        # Retorna os dados serializados como resposta JSON
        return Response(serializer.data)
    @action(detail=True, methods=['get'], url_path='get-inativos')
    def get_inativos(self, request):
        """Traz todos os itens que estão inativos dentro do sistema"""
        cardapio_items = Cardapio.objects.filter(car_status=0).select_related('cat_id')
        
        # Serializa os itens do cardápio
        serializer = CardapioSerializer(cardapio_items, many=True)  # many=True para serializar múltiplos itens
        
        # Retorna os dados serializados como resposta JSON
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        cardapio_item = get_object_or_404(Cardapio, pk)
        cardapio_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['post'], url_path='inativar')
    def inativar(self, request, pk=None):
        """ Inativa um item do cardápio """

        cardapio_item = get_object_or_404(Cardapio, pk=pk)

        cardapio_item.car_status = False  
        cardapio_item.save()

        return Response(
            {"message": f"Item {cardapio_item.nome} foi inativado com sucesso!"},
            status=status.HTTP_200_OK
        )
        
    def update(self, request, pk=None):
        
        cardapio_item = get_object_or_404(Cardapio, pk=pk)
        
        
        serializer = CardapioSerializer(cardapio_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def create(self, request):
        cardapio_itens = CardapioSerializer(data=request.data)
        if cardapio_itens.is_valid():
            cardapio_itens.save()
            return Response(cardapio_itens.data, status=status.HTTP_201_CREATED)

        return Response(cardapio_itens.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        cardapio_item = get_object_or_404(Cardapio, pk=pk)
        serializer = CardapioSerializer(cardapio_item)
        return Response(serializer.data)