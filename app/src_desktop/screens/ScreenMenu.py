import flet as ft
from components.BasePage import BasePage  # Layout base da aplicação
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT  # Constantes de largura e altura
from components.view_container import DynamicContainer  # Container dinâmico
from components.botoes import Button  # Classe personalizada para botões
from screens.layouts_menu.LayoutListAllMenu import LayoutListAllMenu
from screens.layouts_menu.LayoutCategory import LayoutCategory
from screens.layouts_menu.deletar_categoria import TelaDeletarCategoria
from screens.layouts_menu.deletar_menu import TelaDeletarMenu
from screens.layouts_menu.LayoutCreateMenu import LayoutCreateMenu
from components.titles_of_pages import TitlesView


class ScreenMenu(BasePage):
    def __init__(self, page: ft.Page):
        """
        Inicializa a classe Menu com os elementos visuais e configurações.

        Args:
            page (ft.Page): Instância da página principal.
        """
        super().__init__(page)
        self.container_dynamic = DynamicContainer(page=page)  # Instância do container dinâmico
        self.cor_fundo_field_btn = "#2C799F"  # Cor de fundo para o campo de botões
        self.cor_btns = "#1019C2"
        self.title = TitlesView(page)
        

        # Dimensões dos containers
        self.width_container_dinamico = SCREEN_WIDTH * 0.7
        self.height_container_dinamico = SCREEN_HEIGHT * 0.85

        self.width_container_botoes = SCREEN_WIDTH * 0.25
        self.height_container_botoes = SCREEN_HEIGHT * 0.80

        # Criação dos botões
        self.btn_listar_itens = Button(page, color=self.cor_btns)
        self.btn_criar_itens = Button(page, color=self.cor_btns)
        self.btn_remover_itens = Button(page, color=self.cor_btns)
        self.btn_criar_categoria = Button(page, color=self.cor_btns)
        self.remover_categoria = Button(page, color=self.cor_btns)

        # Configuração dos eventos de clique
        self.btn_listar_itens.set_onclick(self.mostrar_listar_itens)
        self.btn_criar_itens.set_onclick(self.mostrar_criar_itens)
        self.btn_remover_itens.set_onclick(self.mostrar_remover_itens)
        self.btn_criar_categoria.set_onclick(self.mostrar_criar_categoria)
        self.remover_categoria.set_onclick(self.mostrar_remover_categoria)
        
        # instanciação das telas de layout
        self.tela_listagem_menu = LayoutListAllMenu(page=page)
        self.tela_listagem_categoria = LayoutCategory(page=page)
        self.tela_deletar_menu=TelaDeletarMenu()
        self.tela_deletar_categoria=TelaDeletarCategoria()
        self.tela_criar_menu=LayoutCreateMenu(page)
        
        
        
    def mostrar_listar_itens(self, e):
        """
        Atualiza o conteúdo dinâmico para mostrar a lista de itens.
        """
        self.container_dynamic.update_content(self.tela_listagem_menu.build())

    def mostrar_criar_itens(self, e):
        """
        Atualiza o conteúdo dinâmico para mostrar a interface de criação de itens.
        """
        self.container_dynamic.update_content(self.tela_criar_menu.build())

    def mostrar_remover_itens(self, e):
        """
        Atualiza o conteúdo dinâmico para mostrar a interface de remoção de itens.
        """
        self.container_dynamic.update_content("Interface para remover itens...")

    def mostrar_criar_categoria(self, e):
        """
        Atualiza o conteúdo dinâmico para mostrar a interface de criação de categorias.
        """
        self.container_dynamic.update_content(self.tela_listagem_categoria.build())

    def mostrar_remover_categoria(self, e):
        """
        Atualiza o conteúdo dinâmico para mostrar a interface de remoção de categorias.
        """
        self.container_dynamic.update_content("Interface para remover categorias...")
        
    def mostrar_editar_menu(self, e):
        self.container_dynamic.update_content(self.tela_editar.build())

    def content(self):
        """
        Constrói o layout completo do menu.

        O layout inclui um cabeçalho, uma barra lateral de botões e um container dinâmico.

        Returns:
            ft.Container: O layout completo como um container do Flet.
        """
        # Cabeçalho (linha superior)
        header_row = ft.Row(
            controls=[
                ft.Container(
                    self.title.build("Menu"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        # Linha principal com a barra de botões e o container dinâmico
        content_row = ft.Row(
            controls=[
                # Barra lateral de botões
                ft.Container(
                    ft.Column(
                        controls=[
                            self.btn_listar_itens.build("Listar Itens"),
                            self.btn_criar_itens.build("Criar Item"),
                            self.btn_remover_itens.build("Remover Item"),
                            ft.Divider(color="white"),
                            self.btn_criar_categoria.build("Criar Categoria"),
                            self.remover_categoria.build("Remover Categoria"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    width=self.width_container_botoes,
                    height=self.height_container_botoes,
                    bgcolor=self.cor_fundo_field_btn,
                    padding=20,
                ),
                # Container dinâmico
                ft.Container(
                    content=self.container_dynamic.get_container(),  # Conteúdo atualizado dinamicamente
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Espaçamento entre os containers
        )

        # Combinação do cabeçalho e da linha principal em um layout vertical
        return ft.Column(
            controls=[header_row, content_row],  # Adiciona as linhas
            spacing=5,  # Espaço entre as linhas
        )

    def buildMenu(self) -> callable:
        return self.build()
