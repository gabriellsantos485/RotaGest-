import flet as ft
from components.BasePage import BasePage
from components.botoes import Button
from components.barra_views_itens import Barra
from config.constant import SCREEN_HEIGHT, SCREEN_WIDTH
from services.APIClient import APIClient

class LayoutListAllMenu(BasePage):
    """
    Classe responsável por criar o layout para listar itens no menu.
    """
    
    def __init__(self, page: ft.Page):
        """
        Inicializa a classe ListarMenu com a página principal.

        Args:
            page (ft.Page): Página principal da aplicação.
        """
        super().__init__(page)
        self.page = page
        self.botao_buscar=Button(page, color="green")
        self.api=APIClient()
        self.barra_menu=Barra(self.api.get_api("http://127.0.0.1:8000/api/menus/"), on_remove=self.__remover_item_callback, page=page)
        
        
    def __remover_item_callback(self, item_id):
        self.api.remove(f"http://127.0.0.1:8000/api/menus/{item_id}/")
    
        
    def content(self) -> ft.Container:
        """
        Constrói o layout da tela de listagem.

        Returns:
            ft.Container: Container com os elementos visuais construídos.
        """
        return ft.Container(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                                ft.TextField(
                                    label="Buscar",  #Placeholder inicial
                                    width=500,
                                    height=40,
                                    bgcolor="white", 
                                    border_radius=10,
                                ),
                            self.botao_buscar.build("Buscar")
                        ]                      
                    ),
                    ft.Row(
                        controls=[
                            self.barra_menu.build()
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
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
            bgcolor="#22094D"
            
        )

    
    def buildListMenu(self):
        self.build()