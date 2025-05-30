from restaurante.models.formapagamento import FormaPagamento
from restaurante.serializers import FormaPagamentoSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status


class FormaPagamentoServices(ViewSet):
    
    def list(self, request): 
        formapagamento = FormaPagamento.objects
        sr = FormaPagamentoSerializer(formapagamento,many=True )
        return Response(sr.data)
        
    def destroy(self, request, pk=None): 
        fpa = get_object_or_404(FormaPagamento, pk=pk)
        fpa.delete()
        return Response(status.HTTP_200_OK)
    
    def update(self, request, pk=None): 
        fpa = get_object_or_404(FormaPagamento, pk=pk)
        sr = FormaPagamentoSerializer(fpa, data=request.data, partial= True)
        
        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_200_OK)
        return Response(sr.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request): 
        sr = FormaPagamentoSerializer(data=request.data)
        
        if sr.is_valid():
            sr.save()
            return Response(sr.data, status=status.HTTP_200_OK)
        return Response(sr.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def cliente_associados(self, request, pk=None): pass
    def formapagamento_mais_usada(self, request): pass
    
    def formapagamento_mais_usada_cliente(self, request, pk=None): pass