import flet as ft  # Importa o módulo Flet
from components.com_appContainer import AppContainer  # Classe para o layout base da aplicação
from components.cards import Card  # Classe para criação de cartões estilizados
from config.constant import SCREEN_HEIGHT, SCREEN_WIDTH  # Constantes de largura e altura da tela
from components.botoes import Button  # Classe personalizada para botões

class HomeScreen:
    """
    Classe responsável por construir e organizar a tela inicial do aplicativo.

    Atributos:
        page (ft.Page): Página principal do aplicativo.
        base (AppContainer): Container base para o layout da tela.
        card1, card2, card3 (Card): Instâncias de cartões estilizados.
        buttons_card1, buttons_card2, buttons_card3 (list): Listas de botões associados a cada cartão.

    Métodos:
        __init__(self, page: ft.Page):
            Inicializa a classe com a configuração inicial dos elementos.
        
        get_widget(self):
            Constrói e retorna o layout principal da tela inicial.
    """

    def __init__(self, page: ft.Page):
        """
        Inicializa a classe HomeScreen.

        Args:
            page (ft.Page): Instância da página principal onde o layout será exibido.
        """
        self.page = page
        self.base = AppContainer(page)  # Container base para o layout

        # Criação e configuração dos cartões
        self.card1 = Card("#44998B", "img\\img_card1.jpeg")
        self.card2 = Card("#121357", "img\\img_card2.png")
        self.card3 = Card("#5E0E4F", "img\\img_card3.jpeg")
        self.card3.set_spacing_btn(10)  # Define o espaçamento entre os botões do terceiro cartão

        # Criação dos botões para cada funcionalidade
        self.btn_ctrl_pedidos = Button(route="/pedidos", page=self.page)
        self.btn_fila_pedidos = Button(route="/menu", page=self.page)
        self.btn_historico_pedidos = Button(route="/menu", page=self.page)

        self.btn_cadastrar_cliente = Button(route="/menu", page=self.page, color="#1019C2")
        self.buscar_cliente = Button(route="/menu", page=self.page, color="#1019C2")
        self.todos_clientes = Button(route="/menu", page=self.page, color="#1019C2")

        self.menu = Button(route="/menu", page=self.page, color="#B61254")
        self.funcionarios = Button(route="/menu", page=self.page, color="#B61254")
        self.pedidos_cancelados = Button(route="/menu", page=self.page, color="#B61254")
        self.outros = Button(route="/menu", page=self.page, color="#B61254")

        # Listas de botões associados a cada cartão
        self.buttons_card1 = [
            self.btn_ctrl_pedidos.build("Controle de Pedidos"),
            self.btn_fila_pedidos.build("Fila de Pedidos"),
            self.btn_historico_pedidos.build("Histórico de Pedidos")
        ]

        self.buttons_card2 = [
            self.btn_cadastrar_cliente.build("Cadastrar Cliente"),
            self.buscar_cliente.build("Buscar Cliente"),
            self.todos_clientes.build("Todos os Clientes")
        ]

        self.buttons_card3 = [
            self.menu.build("Menu"),
            self.funcionarios.build("Funcionários"),
            self.pedidos_cancelados.build("Pedidos Cancelados"),
            self.outros.build("Outros")
        ]

    def get_widget(self):
        """
        Constrói o layout principal da tela inicial.

        O layout inclui três colunas, cada uma contendo um cartão com botões configurados dinamicamente.

        Returns:
            ft.Container: O container principal com todos os elementos organizados.
        """
        content = ft.Container(
            width=SCREEN_WIDTH * 0.85,
            height=SCREEN_HEIGHT * 0.85,
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            self.card1.build(self.buttons_card1)  # Primeiro cartão
                        ]
                    ),
                    ft.Column(
                        controls=[
                            self.card2.build(self.buttons_card2)  # Segundo cartão
                        ]
                    ),
                    ft.Column(
                        controls=[
                            self.card3.build(self.buttons_card3)  # Terceiro cartão
                        ]
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os elementos horizontalmente
            ),
        )

        # Retorna o conteúdo centralizado usando o container base
        return self.base.center_content(self.base.build(content))
