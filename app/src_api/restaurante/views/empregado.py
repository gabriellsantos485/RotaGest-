from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from restaurante.serializers import EmpregadoSerializer
from restaurante.models import Empregado
from rest_framework import status
from django.shortcuts import get_object_or_404 

class EmpregadoService(ViewSet):
    
    def list(self, request):
        empregado = Empregado.objects
        serializer = EmpregadoSerializer(empregado, many=True)

        return Response(serializer.data)
    
    def destroy(self, request, pk):
        empregado = get_object_or_404(Empregado, pk)
        empregado.delete()
    
    def update(self, request, pk=None):
        empregado = get_object_or_404(Empregado, pk=pk)
        
        empregado = EmpregadoSerializer(empregado, data=request.data, partial=True)
        if empregado.is_valid():
            empregado.save()
            return Response(empregado.data, status=status.HTTP_200_OK)
        return Response(empregado.data, status=status.HTTP_400_BAD_REQUEST)
        
       
    
    def create(self, request):
        empregado = EmpregadoSerializer(data=request.data)
        if empregado.is_valid():
            empregado.save()
            return Response(empregado.data, status=status.HTTP_201_CREATED)
    
        return Response(empregado.errors, status.HTTP_400_BAD_REQUEST)