import flet as ft
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT


class CustomNavBar:
    def __init__(self, page):
        """
        Classe para criar uma barra de navegação personalizada.
        """
        self.page=page
        self.__width=SCREEN_WIDTH
        self.__height=SCREEN_HEIGHT*0.10
        self.__border_radios=0

    def render(self):
        """
        Método para renderizar a barra de navegação.

        Returns:
            ft.Row: Componente Flet representando a barra de navegação.
        """
        return ft.Container(
            content=ft.Row(
                controls=[
                    # Ícone Pessoas à esquerda
                    ft.IconButton(
                        icon=ft.icons.PEOPLE,
                        on_click=lambda e: self.page.go("/clients"),
                        tooltip="Pessoas",
                        bgcolor=ft.colors.WHITE,
                        opacity=self.get_icon_opacity("/clients")
                    ),
                    # Espaço flexível para centralizar o próximo item
                    ft.Container(expand=1),
                    # Ícone Home centralizado
                    ft.IconButton(
                        icon=ft.icons.HOME,
                        on_click=lambda e: self.page.go("/category"),
                        tooltip="Home",
                        bgcolor=ft.colors.WHITE,
                        opacity=self.get_icon_opacity("/category")
                    ),
                    # Espaço flexível para centralizar o próximo item
                    ft.Container(expand=1),
                    # Ícone Sacola à direita
                    ft.IconButton(
                        icon=ft.icons.SHOPPING_BAG,
                        on_click=lambda e: self.page.go("/bag"),
                        tooltip="Sacola",
                        bgcolor=ft.colors.WHITE,
                        opacity=self.get_icon_opacity("/bag")
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor="#4E7CF0",  # Cor de fundo
            border_radius=self.__border_radios,
            width=self.__width,
            height=self.__height
        )
    
    def set_width(self, new_width: int)-> ft.Page.width:
        """
        Set the width of navbar
        
        new_width: the new number of new width
        
        returns: the new width of container 
        """
        
        self.__width=new_width
        return self.__width
    
    def set_height(self, new_height):
        self.__height = new_height
        return self.__height
    
    def border_radius(self, var):
        if var == True:
            self.border_radius=20
        return self.border_radius
    
    def get_icon_opacity(self, route: str) -> float:
        """
        Define a opacidade do ícone com base na rota ativa.

        Args:
            route (str): A rota associada ao ícone.

        Returns:
            float: Opacidade do ícone (1.0 para ativo, 0.5 para inativo).
        """
        return 1.0 if self.page.route == route else 0.5
    

