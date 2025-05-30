from rest_framework import serializers
from .models import (
    Cardapio, Comanda, Cliente, Estoque, Mesa, Empregado, Usuario, Categoria, FormaPagamento, Ingrediente, Pedido, ItemMenu
    )
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

class CardapioSerializer(serializers.ModelSerializer):
    #categoria = serializers.CharField(source='cat_id.cat_nome')  # Acessa o nome da categoria, sem a necessidade de selecionar manualmente
    """exemplo de usu :
     
    {
        
    "car_nome": "Empadad de frango",
    "car_valor": 5.58,
    "categoria": 50,
    "cat_id": 1
    
    }
"""
    class Meta:
        model = Cardapio
        fields = ['car_nome', 'car_valor'   , 'cat_id', 'car_id']  # Campos que queremos retornar

    def create(self, validate_data):
        cardapio = Cardapio.objects.create(
            car_nome = validate_data['car_nome'],
            car_valor = validate_data['car_valor'],
            cat_id = validate_data['cat_id']
        )
        
        return cardapio

class ClienteSerializer(serializers.ModelSerializer):
    cli_rua = serializers.CharField(allow_null=True, required=False)
    cli_numeroCasa = serializers.CharField(allow_null=True, required=False)
    cli_complemento = serializers.CharField(allow_null=True, required=False)
    cli_bairro = serializers.CharField(allow_null=True, required=False)
    cli_cidade = serializers.CharField(allow_null=True, required=False)
    cli_estado = serializers.CharField(allow_null=True, required=False)
    cli_id = serializers.CharField(allow_null=True, required=False)
    
    class Meta:
        model = Cliente
        fields = ['cli_nome', 'cli_email', 
                  'cli_sobrenome', 'cli_telefone', 
                  'cli_dataNascimento', 'cli_rua', 
                  'cli_numeroCasa', 'cli_complemento',
                  'cli_bairro', 'cli_cidade',
                  'cli_estado', 'cli_id']
        
class EmpregadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Empregado
        fields = ['emp_nome', "emp_horarioTrabalho", 'emp_sobrenome', 'emp_rua', 'emp_bairro', 'emp_cidade', 'emp_estado', 'emp_salario', 'emp_dataAniversario', 'usu_id']
                
class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario # Corrigido: Atribui o modelo User ao atributo model
        fields = ('usu_username', 'usu_password', 'usu_telefone', 'usu_email', 'usu_isAdmin')  # Inclui todos os campos do modelo
        extra_kwargs = {'usu_password': {'write_only': True}}  # Garante que a senha não seja retornada na resposta
        
    def create(self, validated_data):
        password = validated_data.pop('usu_password')
        hashed_password = make_password(password)
        usuario = Usuario.objects.create(
            usu_username=validated_data['usu_username'],
            usu_telefone=validated_data['usu_telefone'],
            usu_email=validated_data['usu_email'],
            usu_password=hashed_password,
            usu_isAdmin=validated_data.get('usu_isAdmin', False)
        )
        return usuario
        
class LoginSerializer(serializers.Serializer):
    
    usu_username = serializers.CharField()
    usu_password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('usu_username')
        password = data.get('usu_password')

        try:
            user = Usuario.objects.get(usu_username=username) # Obtem o usuário pelo nome de usuário
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Usuário não encontrado.")
        
        if not user.check_password(password): # Verifica a senha
            raise serializers.ValidationError("Senha incorreta.")

        data['user'] = user  # Adiciona o objeto usuário aos dados validados
        return data
    
class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ["cat_nome",'cat_id']
        
class PedidoSerializer(serializers.ModelSerializer):
    pass

class MesaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mesa
        fields = ['mesa_id','mesa_status']

class ComandaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comanda
        fields = ['com_id', 'com_status']

class ItemPedido(serializers.ModelSerializer):
    pass

class FormaPagamentoSerializer(serializers.ModelSerializer):
    fpa_id = serializers.CharField(allow_null = True, required=False)
    
    class Meta:
        model = FormaPagamento
        fields = ['fpa_id', 'fpa_forma']
        
class IngredienteSerializer(serializers.ModelSerializer):
    ing_id = serializers.CharField(allow_null = True, required = False)
    
    class Meta:
        model = Ingrediente
        fields = ['ing_id', 'ing_nome']
        
class PedidoSerializer(serializers.ModelSerializer):
    ped_id = serializers.CharField(allow_null = True, required = False)
    ped_valorTotal = serializers.CharField(allow_null = True, required = False)
    ped_dataFechamento = serializers.CharField(allow_null = True, required = False)
    ped_dataAbertura = serializers.CharField(allow_null = True, required = False)
    ped_status = serializers.CharField(allow_null = True, required = False)
    
    class Meta:
        model = Pedido
        fields = ['ped_id', 'ped_dataAbertura', 'ped_dataFechamento', 'ped_status', 'ped_valorTotal',
                  'cli_id', 'mesa_id', 'com_id', 'emp_id', 'fpa_id',]
        
class ItemPedidoSerializer(serializers.ModelSerializer):
    ite_id = serializers.CharField(allow_null = True, required = False)
    class Meta:
        model = ItemMenu
        fields = ['ite_id', 'ite_qtde', 'ite_valor', 'ped_id', 'car_id']

class EstoqueSerializer(serializers.ModelSerializer):
    est_id = serializers.CharField(allow_null = True, required = False)
    
    class Meta:
        model = Estoque
        fields = ['est_id', 'est_qtde', 'est_validade', 'est_dataAtual', 'ing_id', 'car_id']

    