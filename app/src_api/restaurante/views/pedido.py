from restaurante.models.pedido import Pedido
from .itempedido import ItemPedidoServices
from .comanda import ComandaServices
from .mesa import MesaServices
from restaurante.serializers import PedidoSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status

class PedidoServices(ViewSet):
    def list(self, request): 
        pedido = Pedido.objects
        sr = PedidoSerializer(pedido, many = True)
        return Response(sr.data)

    def create(self, request): 
        sr = PedidoSerializer(data=request.data)
        if sr.is_valid():
            sr.save()
            comanda = sr.data['com_id']
            self.__modificar_status_comanda(comanda)
            return sr.data['ped_id']
        return Response(sr.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def __modificar_status_comanda(self, pk):
        comanda = ComandaServices
        comanda.modificar_status(pk=pk)
        
    
    def modificar_status_mesa(self):
        mesa = MesaServices
        
    
    @action(detail=True, methods=['put'], url_path='status-pedido')
    def modificar_status_pedido(self, request, pk=None):
        pedido = get_object_or_404(Pedido, pk=pk)
        pedido.ped_status = "F"
        pedido.save()
        comanda = pedido.com_id.pk
        self.__modificar_status_comanda(comanda)
        return Response(status=status.HTTP_200_OK)
    
    def retornar_valor_total(self):
        pass
    
    @action(detail=True, methods=['put'], url_path='metodo-pagamento')
    def modificar_metodo_pagamento(self, request, pk=None):
        pedido = get_object_or_404(Pedido, pk=pk)
        pedido.fpa_id = 0
        pedido.save()
        return Response(status=status.HTTP_200_OK)
    
    def modificar_valor_total(self):
        pass
    
    def itens_pedidos(self):
        pass