import flet as ft
from flet import Container, Text, Row, Column, IconButton, icons, MainAxisAlignment, Page
from config.constant import SCREEN_WIDTH
from components.BasePage import BasePage
from components.OrderPaymentDialog import OrderPaymentDialog
from services.APIClient import APIClient

"""
    Arquivo responsável por renderizar uma tabela dinâmica com cabeçalhos fixos.
    Implementa métodos para adicionar dados à tabela, registrar callbacks para os botões de pagamento e cancelamento,
    e renderizar a tabela na tela.
"""

class TableView:
    """
    Classe para criar uma tabela dinâmica com cabeçalhos fixos e dados dinâmicos.
    """

    def __init__(self, page: Page, cabecalhos: list, largura: int = None):
        """
        Inicializa a tabela com cabeçalhos fixos.

        Args:
            page (Page): Página onde a tabela será renderizada.
            cabecalhos (list): Lista de strings representando os cabeçalhos.
            largura (int): Largura da tabela (opcional).
        """
        self.page = page
        self.cabecalhos = cabecalhos + ["Ações"]  # Adiciona a coluna "Ações"
        self.largura = largura or page.width
        self.__dados = []
        self.__on_pagamento = None
        self.__on_cancelamento = None

    def set_dados(self, dados: list) -> str:
        """Define os dados dinâmicos da tabela."""
        self.__dados = dados

    def on_pagamento_click(self, callback) -> str:
        """Registra um callback para o botão de pagamento."""
        self.__on_pagamento = callback

    def on_cancelamento_click(self, callback) -> callable:
        """Registra um callback para o botão de cancelamento."""
        self.__on_cancelamento = callback

    def _obter_pedido_id(self, linha_dados) -> str:
        """
        Obtém o ID do pedido a partir dos dados da linha.
        """
        return linha_dados.get("N° do Pedido", None)
    
    def __obter_valor_total(self, linha_dados) -> str:
        return linha_dados.get("Valor Total", None)

    def _criar_botoes_acao(self, linha_dados) ->Row:
        """
        Cria os botões de ação para a linha da tabela.
        """
        pedido_id = self._obter_pedido_id(linha_dados)
        total = self.__obter_valor_total(linha_dados)
        return Row(
            controls=[
                IconButton(
                    icon=icons.PAYMENTS,
                    tooltip="Efetuar Pagamento",
                    icon_color="green",
                    on_click=lambda _: self.efetuar_pagamento(pedido_id, total),
                ),
                IconButton(
                    icon=icons.CANCEL,
                    tooltip="Cancelar Pedido",
                    icon_color="red",
                    on_click=lambda _: self.cancelar_pedido(pedido_id),
                ),
            ],
            alignment=MainAxisAlignment.END,
        )

    def _criar_cabecalhos(self) -> ft.Row:
        """
        Cria a linha de cabeçalhos.
        """
        return Row(
            controls=[
                Text(cabecalho, size=16, weight="bold", color="white")
                for cabecalho in self.cabecalhos
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
        )

    def _criar_linha(self, linha_dados: dict) -> Container:
        """
        Cria uma linha com base nos dados.
        """
        botoes = self._criar_botoes_acao(linha_dados)

        return Container(
            content=Row(
                controls=[
                    Text(str(linha_dados.get(campo, "")), size=14, color="black")
                    for campo in self.cabecalhos[:-1]
                ]
                + [botoes],  # Adiciona os botões como última coluna
                alignment=MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=10,
            bgcolor="#f0f0f0",
            border_radius=5,
        )

    def build(self) -> Column: 
        """
        Constrói a tabela completa.
        """
        linhas = [self._criar_linha(dados) for dados in self.__dados]
        return Column(
            controls=[self._criar_cabecalhos()] + linhas,
            spacing=10,
            width=SCREEN_WIDTH,
        )

    def __validar_senha(self, senha, pedido_id) -> None:
        """
        Valida a senha antes de cancelar o pedido.
        """
        if senha == "teste":
            print(f"Pedido {pedido_id} cancelado com sucesso!")
            # self.base.mensagens_dialog("Pedido cancelado com sucesso.", tipo="success", conf=False)
        else:
            pass
        """
        Exibe o diálogo solicitando a senha do administrador para cancelar o pedido.
        """
        
    def efetuar_pagamento(self, pedido_id, total)->None:
        api=APIClient()
        data_orders_items=api.get_api(f"http://127.0.0.1:8000/api/itens-menu/filtrar_por_ped_id/?ped_id={pedido_id}")
        
        #dialog responsable of screen of payment
        opd = OrderPaymentDialog(self.page, pedido_id, data_orders_items, total)
        """
        Realiza a ação de pagamento do pedido.
        """
        print(f"Pagamento do pedido {pedido_id} realizado.")
        opd.open_dialog()
        # Aqui você pode adicionar a lógica para efetuar o pagamento
        
        
# [{'menu_id': 1, 'quantidade': 3}, {'menu_id': 6, 'quantidade': 2}, {'menu_id': 10, 'quantidade': 1}, {'menu_id': 11, 'quantidade': 3}, {'menu_id': 12, 'quantidade': 1}, {'menu_id': 13, 'quantidade': 2}]