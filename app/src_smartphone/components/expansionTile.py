import flet as ft
from config.constant import SCREEN_WIDTH

# Definição da classe Category
class Category:
    def __init__(self, title, items, width=200, height=40):
        """
        Classe para representar uma categoria com uma lista de sub-itens.

        Args:
            title (str): O título da categoria.
            items (list): Lista de itens dentro da categoria.
            width (int, optional): Largura dos itens. Default: 200.
            height (int, optional): Altura dos itens. Default: 40.
        """
        self.title = title
        self.items = items
        self.width = width
        self.height = height
        self.color=ft.colors.WHITE

    def render(self):
        controls = [
            item if isinstance(item, ft.Control)  # Verifica se o item já é um componente visual
            else ft.Container(
                content=ft.Text(item),
                width=self.width,
                height=self.height,
                bgcolor="#F3F3F3",
                border_radius=5,
                padding=10,
                margin=5,
                
            )
            for item in self.items
        ]

        return ft.Container(
        content=ft.Container(  
            content=ft.ExpansionTile(
                title=ft.Text(self.title, weight=ft.FontWeight.BOLD, color=self.color),
                controls=controls,
                text_color="#4A4A4A",
                collapsed_text_color="#9E9E9E",
                width=SCREEN_WIDTH *0.95,
            ),
            bgcolor="transparent",  
        ),
        bgcolor="#5C0B64",  
        border_radius=20,
    )
        

class CategoryList:
    def __init__(self, categories):
        """
        Classe para renderizar uma lista de categorias.

        Args:
            categories (list): Lista de objetos Category.
        """
        self.categories = categories

    def render(self):
        """
        Renderiza a lista de categorias.

        Returns:
            list: Lista de componentes ExpansionTile.
        """
        return [category.render() for category in self.categories]

# Lista de categorias para serem exibidas

