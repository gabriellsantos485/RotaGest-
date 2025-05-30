from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status
from restaurante.models.mesa import Mesa
from restaurante.serializers import MesaSerializer

class MesaServices(ViewSet):
    def list(self, request):
        mesa = Mesa.objects
        sr = MesaSerializer(mesa, many=True)
        return Response(sr.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        mesa = get_object_or_404(Mesa, pk=pk)
        mesa.delete()
        
        Response(status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        mesa = get_object_or_404(Mesa, pk=pk)
        sr = MesaSerializer(mesa, data=request.data, partial=True)
        
        if sr.is_valid():
            if mesa.mesa_status == 1:
                mesa.mesa_status = False
                mesa.save()
                return Response(sr.data, status=status.HTTP_200_OK)
            mesa.mesa_status = True
            mesa.save()
            return Response(sr.data, status=status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
    
    def create(self, request):

        mesa= MesaSerializer(data=request.data)
        if mesa.is_valid():
            mesa.save()
            return Response(mesa.data, status=status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'], url_path='pedido-associado')
    def pedido_associado(self, request, pk=None):
        pass
    
    @action(detail=True, methods=['get'], url_path='valor-mesa')
    def valor_mesa(self, request, pk=None):
        pass
    
    @action(detail=True, methods=['get'], url_path='pessoas-associadas')
    def pessoas_associadas(self, request, pk=None):
        pass
    
    @action(detail=True, methods=['get'], url_path='cliente-aniversario')
    def verificar_mesa_aniversario_cliente(self):
        query = "SELECT ..."
        

    