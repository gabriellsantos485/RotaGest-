from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from restaurante.models.comanda import Comanda
from restaurante.serializers import ComandaSerializer

class ComandaServices(ViewSet):
    
    def list(self, request):
        comanda = Comanda.objects
        sr = ComandaSerializer(comanda, many=True)
        return Response(sr.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        comanda = get_object_or_404(Comanda, pk=pk)
        comanda.delete()
        Response(status.HTTP_200_OK)
    
    def update(self, request, pk):
        comanda = get_object_or_404(Comanda, pk=pk)
        sr = ComandaSerializer(comanda, data=request.data)
        
        if sr.is_valid():
            comanda.save()
            return Response(sr.data, status.HTTP_200_OK)
        
        return Response(status.HTTP_400_BAD_REQUEST)
    
    def create(self, request):
        sr = ComandaSerializer( data=request.data)
        
        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_200_OK)
        return Response(sr.data, status.HTTP_400_BAD_REQUEST)
    
    def aniversario_cliente(self, request):
        query = None
    
    def whatssapp_cliente(self, request):
        query = "SELECT cliente.telefone FROM cliente"
    
    @staticmethod
    def modificar_status(pk):
        comanda = get_object_or_404(Comanda, pk=pk) 
        if comanda.com_status == False:
            comanda.com_status = True
            return comanda.save()
        
        comanda.com_status=False
        return comanda.save()

    
        
    
