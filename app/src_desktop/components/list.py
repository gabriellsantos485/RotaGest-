import flet as ft
from flet import Container, Text, Row, Column, IconButton, icons, MainAxisAlignment, Page
from config.constant import SCREEN_WIDTH
from components.com_appContainer import AppContainer

class TabelaDinamica:
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
        self.base=AppContainer(page)

    def set_dados(self, dados: list):
        """
        Define os dados dinâmicos da tabela.

        Args:
            dados (list): Lista de dicionários com os dados a serem exibidos.
        """
        self.__dados = dados

    def on_pagamento_click(self, callback):
        """
        Registra um callback para o botão "Efetuar Pagamento".

        Args:
            callback (function): Função chamada ao clicar no botão de pagamento.
        """
        self.__on_pagamento = callback

    def on_cancelamento_click(self, callback):
        """
        Registra um callback para o botão "Cancelar Pedido".

        Args:
            callback (function): Função chamada ao clicar no botão de cancelamento.
        """
        self.__on_cancelamento = callback

    def _criar_cabecalhos(self):
        """
        Cria a linha de cabeçalhos.

        Returns:
            Row: Linha contendo os cabeçalhos.
        """
        return Row(
            controls=[
                Text(cabecalho, size=16, weight="bold", color="white")
                for cabecalho in self.cabecalhos
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            
        )

    def _criar_linha(self, linha_dados: dict):
        """
        Cria uma linha com base nos dados.

        Args:
            linha_dados (dict): Dicionário com os dados da linha.

        Returns:
            Container: Linha formatada.
        """
        # Botões para ações
        botoes = Row(
            controls=[
                IconButton(
                    icon=icons.PAYMENTS,
                    tooltip="Efetuar Pagamento",
                    icon_color="green",
                    on_click=lambda _: self.page.go("/pagamento")
                ),
                IconButton(
                    icon=icons.CANCEL,
                    tooltip="Cancelar Pedido",
                    icon_color="red",
                    on_click=self.cancelar_pedido
                ),
            ],
            alignment=MainAxisAlignment.END,
        )

        # Linha com os dados e botões
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

    def build(self):
        """
        Constrói a tabela completa.

        Returns:
            Column: Tabela com cabeçalhos e linhas.
        """
        linhas = [self._criar_linha(dados) for dados in self.__dados]
        return Column(
            controls=[self._criar_cabecalhos()] + linhas,
            spacing=10,
            width=SCREEN_WIDTH
        )
    def __password(self, senha):
        """
        Valida a senha e exibe uma mensagem de confirmação ou erro.
        """
        if senha == 'teste':
            print(senha) #self.base.mensagens_dialog("Senha correta. Pedido cancelado com sucesso.", tipo="success", conf=False)
        else:
            self.base.mensagens_dialog("Senha incorreta. Tente novamente.", tipo="error", conf=False)

    def cancelar_pedido(self, e):
        """
        Exibe o diálogo solicitando a senha do administrador para cancelar o pedido.
        """
        self.base.mensagens_dialog(
            "Para CANCELAR o pedido, digite a senha de administrador:",
            tipo="alert",
            conf=True,
            on_confirm=self.__password,  # Passa o callback corretamente
        )

            