from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from restaurante.models.itemmenu import ItemMenu
from restaurante.serializers import ItemPedidoSerializer

class ItemPedidoServices(ViewSet):
    
    def list(self, request): 
        ite = ItemMenu.objects
        sr = ItemPedidoSerializer(ite, many=True)
        return Response(sr.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk): 
        ite = get_object_or_404(ItemMenu, pk=pk)
        ite.delete()
        return Response(status.HTTP_200_OK)
    
    def update(self, request): 
        ite = get_object_or_404(ItemMenu, pk=request.data['ite_id'])
        sr = ItemPedidoSerializer(ite, data=request.data)
        
        if sr.is_valid():
            sr.save()
            return Response(sr.data, status.HTTP_200_OK)
        
        return Response(status.HTTP_400_BAD_REQUEST)
    
    def create(self, request): 
        sr = ItemPedidoSerializer(data=request.data)
        
        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_200_OK)
        return Response(sr.data, status=status.HTTP_400_BAD_REQUEST)
    