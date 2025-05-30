from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from restaurante.models.estoque import Estoque
from restaurante.serializers import EstoqueSerializer

class EstoqueServices(ViewSet):
    """
    ViewSet para o modelo Estoque.
    """
    def list(self, request):
        """
        Retorna todos os registros de estoque.
        """
        estoque = Estoque.objects.all()
        serializer = EstoqueSerializer(estoque, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """
        Retorna um registro de estoque específico.
        """
        estoque = get_object_or_404(Estoque, pk=pk)
        serializer = EstoqueSerializer(estoque)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        Cria um novo registro de estoque.
        """
        serializer = EstoqueSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def __verificar_estoque(self, pk):
        item = get_object_or_404(Estoque, pk=pk)
        if item.est_qtde <= 10:
            return Response({"message": "Estoque baixo"}, status=status.HTTP_200_OK)
        return 
    
    def update(self, request, pk=None):
        """
        Atualiza um registro de estoque existente.
        """
        estoque = get_object_or_404(Estoque, pk=pk)
        serializer = EstoqueSerializer(estoque, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            self.__verificar_estoque(pk=pk)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)