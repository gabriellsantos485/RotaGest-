from restaurante.models.ingrediente import Ingrediente
from restaurante.serializers import IngredienteSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status


class IngredienteServices(ViewSet):
    def list(self, request): 
        ingredientes = Ingrediente.objects
        sr = IngredienteSerializer(ingredientes, many=True)
        return Response(sr.data)
    
    def destroy(self, request, pk=None): 
        ingrediente = get_object_or_404(Ingrediente, pk=pk)
        ingrediente.delete()
        Response(status=status.HTTP_200_OK)
        
    
    def update(self, request, pk=None): 
        ingrediente = get_object_or_404(Ingrediente, pk=pk)
        sr = IngredienteSerializer(ingrediente, data=request.date, partial=True)
        
        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_200_OK)
        return Response(sr.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request): 
        sr = IngredienteSerializer(data=request.data)
        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_200_OK)
        return Response(sr.errors, status=status.HTTP_400_BAD_REQUEST)