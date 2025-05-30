from restaurante.models.cliente import Cliente
from restaurante.serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status

class ClienteService(ViewSet):
    
    def list(self, request): 
        cliente = Cliente.objects
        sr = ClienteSerializer(cliente, many=True)
        return Response(sr.data)
    
    def destroy(self, request, pk=None): 
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.delete()
        return Response(status.HTTP_200_OK)
        
    
    def update(self, request, pk=None): 
        cliente = get_object_or_404(Cliente, pk=pk)
        sr = ClienteSerializer(cliente, data=request.data, partial = True)
        
        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_200_OK)
        return Response(sr.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request): 
        sr = ClienteSerializer(data=request.data)
        
        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_200_OK)
        return Response(sr.errors, status=status.HTTP_400_BAD_REQUEST)
    
    