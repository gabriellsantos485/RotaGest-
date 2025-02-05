import flet as ft
from components.com_appContainer import AppContainer
from components.botoes import Button
from components.barra_views_itens import Barra
from config.constant import SCREEN_HEIGHT, SCREEN_WIDTH

itens = [
    {"id": 1, "nome": "Pizza", "valor": 29.99},
    {"id": 2, "nome": "Hambúrguer", "valor": 19.99},
    {"id": 3, "nome": "Refrigerante", "valor": 5.99},
    {"id": 4, "nome": "Sobremesa", "valor": 12.49},
]


class Menu:
    
    def __init__(self, page: ft.Page):
        """
        Inicializa a classe ListarMenu com a página principal.

        Args:
            page (ft.Page): Página principal da aplicação.
        """
        self.page = page
        self.base = AppContainer(self.page)
        self.botao_buscar=Button(page, color="green")
        self.barra_menu=Barra(itens)
    
    def listar(self):
        """
        Constrói o layout da tela de listagem.

        Returns:
            ft.Container: Container com os elementos visuais construídos.
        """
        content = ft.Container(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                                    ft.TextField(
                                label="Buscar",  #Placeholder inicial
                                width=500,
                                height=40,
                                bgcolor="white",  # Cor corrigida
                                border_radius=10,
                            ),
                            self.botao_buscar.build("Buscar")
                        ]                      
                    ),
                    ft.Row(
                        controls=[
                            self.barra_menu.build()
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.START,  # Ajusta alinhamento horizontal
            ), 
              # Espaçamento interno
            ft.Container(
                bgcolor=ft.colors.RED
            ),
            #padding=20,
            width= SCREEN_WIDTH * 0.65,
            height= SCREEN_HEIGHT * 0.85,
        )
        # Retorna o conteúdo construído
        return self.base.build(content=content)
    
    
    def criarTelaMenu(self, args):
        content = None
        self.base.build(content=content)
    
    def removerMuitosTela(self):
        pass
    
    def criarTelaCategoria(self):
        pass
    
    def removerTelaCategoria(self):
        pass

    