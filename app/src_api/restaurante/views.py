from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import (
    Comanda, FormaPagamento,
    Pedido, Categoria, Menu, ItemMenu, Cliente
)
from .serializers import (
    ComandaSerializer, FormaPagamentoSerializer,
    PedidoSerializer, CategoriaSerializer, MenuSerializer, ItemMenuSerializer, ClienteSerializer
)


class ComandaViewSet(viewsets.ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer

    @action(detail=True, methods=['patch'], permission_classes=[AllowAny])
    def atualizar_status(self, request, pk=None):
        """
        Modifica o status da comanda pelo ID.
        """
        try:
            comanda = self.get_object()
            comanda.com_status = 1
            comanda.save()
            return Response(
                {"message": "Status da comanda atualizado com sucesso!"},
                status=status.HTTP_200_OK,
            )
        except Comanda.DoesNotExist:
            return Response(
                {"error": "Comanda não encontrada."}, status=status.HTTP_404_NOT_FOUND
            )
            
            
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.filter(cli_isActive=True)
    serializer_class = ClienteSerializer

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def adicionar_cliente(self, request):
        """
        Insere um novo cliente no banco de dados.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Cliente adicionado com sucesso!", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )
        
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def get_nome(self, request):
        """
        Retorna o nome de um cliente com base no ID fornecido como parâmetro na URL.
        
        Exemplo de chamada:
        GET /api/clientes/get_nome/?id=1
        """
        cliente_id = request.query_params.get("id")  # Obtém o ID do cliente da URL
        
        if not cliente_id:
            return Response(
                {"error": "O parâmetro 'id' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            cliente = Cliente.objects.get(cli_id=cliente_id, cli_isActive=True)  # Busca o cliente ativo pelo ID
            return Response({"nome": cliente.cli_nome}, status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            return Response(
                {"error": f"Cliente com o ID '{cliente_id}' não encontrado ou está inativo."},
                status=status.HTTP_404_NOT_FOUND
            )


class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer

    def list(self, request, *args, **kwargs):
        formas_pagamento = self.get_queryset()
        serializer = self.get_serializer(formas_pagamento, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        forma_pagamento = self.get_object()
        forma_pagamento.delete()
        return Response({"message": "Forma de pagamento excluída com sucesso"}, status=status.HTTP_200_OK)


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.filter(ped_status='A')
    serializer_class = PedidoSerializer

    def list(self, request, *args, **kwargs):
        pedidos = self.get_queryset()
        serializer = self.get_serializer(pedidos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Cria um novo pedido e retorna o ID do pedido criado junto com os dados.
        """
        data = request.data.copy()  # Cria uma cópia mutável do QueryDict
        data['ped_status'] = 'A'  # Adiciona o valor do campo ped_status
        serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            pedido = serializer.save()  # Salva o pedido e obtém a instância do modelo
            response_data = {
                "data": {
                    "ped_id": pedido.ped_id,  # Obtém o ID do pedido criado
                    **serializer.data,  # Inclui os dados serializados
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            pedido = self.get_object()
            pedido.ped_status = 'C'
            pedido.save()
            return Response({"message": "Pedido cancelado com sucesso"}, status=status.HTTP_200_OK)
        except Pedido.DoesNotExist:
            return Response({"error": "Pedido não encontrado"}, status=status.HTTP_404_NOT_FOUND)



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @action(detail=False, methods=['post'])
    def criar_categoria(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(menu_status=True)
    serializer_class = MenuSerializer

    def list(self, request, *args, **kwargs):
        """
        Retorna a lista de menus em ordem alfabética, 
        filtrando apenas aqueles com 'menu_status=True'.
        """
        menus = self.get_queryset().filter(menu_status=True).order_by('menu_nome')
        serializer = self.get_serializer(menus, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request, *args, **kwargs):
        """
        Método para criar um novo menu.
        """
        data = request.data.copy()  # Cria uma cópia mutável do QueryDict
        data["menu_status"] = True
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Método para desativar um menu (soft delete).
        """
        try:
            menu = self.get_object()
            menu.menu_status = False
            menu.save()
            return Response(
                {"message": "Menu desativado com sucesso"}, status=status.HTTP_200_OK
            )
        except Menu.DoesNotExist:
            return Response(
                {"error": "Menu não encontrado"}, status=status.HTTP_404_NOT_FOUND
            )
            
    def update(self, request, *args, **kwargs):
        """
        Método para atualizar os dados de um menu.
        """
        try:
            # Obtém o objeto do menu com base no ID (pk)
            menu = self.get_object()
            
            # Atualiza os campos do menu com os dados enviados
            serializer = self.get_serializer(menu, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Menu atualizado com sucesso", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Menu.DoesNotExist:
            return Response(
                {"error": "Menu não encontrado"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"Ocorreu um erro ao atualizar o menu: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
    @action(detail=False, methods=['get'])
    def listar_por_categoria(self, request):
        """
        Retorna os menus organizados por categoria no formato especificado:
        [
            {"Categoria1": {"item1": valor1, "item2": valor2}},
            {"Categoria2": {"item3": valor3, "item4": valor4}}
        ]
        """
        menus = self.get_queryset().filter(menu_status=True)
        categorias = {}

        for menu in menus:
            categoria_nome = menu.cat_id.cat_nome  # Assumindo que `menu_categoria` é um campo relacionado ao modelo Categoria
            if categoria_nome not in categorias:
                categorias[categoria_nome] = {}
            categorias[categoria_nome][menu.menu_nome] = menu.menu_valor

        resultado = [{categoria: itens} for categoria, itens in categorias.items()]
        return Response(resultado, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def buscar_por_nome(self, request):
        """
        Pesquisa um menu pelo nome e retorna o ID correspondente.

        Exemplo de chamada:
        GET /api/menus/buscar_por_nome/?nome=Pizza

        Retorno:
        - ID do menu, caso encontrado.
        - Mensagem de erro, caso contrário.
        """
        nome = request.query_params.get("nome")
        if not nome:
            return Response(
                {"error": "O parâmetro 'nome' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            menu = self.get_queryset().get(menu_nome=nome)
            return Response({"id": menu.menu_id}, status=status.HTTP_200_OK)
        except Menu.DoesNotExist:
            return Response(
                {"error": f"Menu com o nome '{nome}' não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
            
class ItemMenuViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar os itens do menu.
    """
    queryset = ItemMenu.objects.all()
    serializer_class = ItemMenuSerializer

    def list(self, request, *args, **kwargs):
        """
        Retorna a lista de itens do menu.
        """
        itens = self.get_queryset()
        serializer = self.get_serializer(itens, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Cria um novo item no menu.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Deleta (soft delete) um item do menu, alterando seu status para inativo.
        """
        try:
            item = self.get_object()
            item.status = False  # Supondo que o modelo tenha um campo `status` para soft delete
            item.save()
            return Response(
                {"message": "Item desativado com sucesso."},
                status=status.HTTP_200_OK
            )
        except ItemMenu.DoesNotExist:
            return Response(
                {"error": "Item não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
            
    @action(detail=False, methods=['get'])
    def filtrar_por_ped_id(self, request):
        """
        Filtra os itens do menu pelo `ped_id` e retorna o `menu_id` com a quantidade correspondente.
        """
        ped_id = request.query_params.get('ped_id')
        if not ped_id:
            return Response({"error": "O parâmetro 'ped_id' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        itens_filtrados = (
            ItemMenu.objects.filter(ped_id=ped_id)
            .values('menu_id')
            .annotate(quantidade=Sum('ime_qtde'))  # Soma o campo ime_qtde
        )

        return Response(itens_filtrados, status=status.HTTP_200_OK)