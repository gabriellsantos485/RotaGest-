from rest_framework import serializers
from .models import Cliente, Comanda, FormaPagamento, Pedido, Categoria, Menu, ItemMenu


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'cli_id', 'cli_nome', 
            'cli_isActive'
        ]


class ComandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comanda
        fields = [
            'com_id', 
            'com_status'
        ]


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = [
            'ped_id', 
            'ped_abertura',  # Campo renomeado para "abertura"
            'ped_fechamento',  # Campo adicionado para "fechamento"
            'ped_status', 
            'ped_valorTotal', 
            'cli_id', 
            'fpa_id', 
            'com_id',  # Relacionamento com Comanda
        ]


class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = [
            'fpa_id', 
            'fpa_tipo'
        ]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = [
            'cat_id', 
            'cat_nome'
        ]


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            'menu_id', 
            'menu_nome', 
            'menu_valor', 
            'menu_status', 
            'menu_descricao', 
            'menu_imagem', 
            'cat_id'
        ]


class ItemMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMenu
        fields = [
            'ime_id', 
            'ime_valorUnitario', 
            'ime_qtde', 
            'ped_id', 
            'menu_id'
        ]
