import flet as ft
from flet import Container, Column, Text, ExpansionTile, Row, IconButton, ElevatedButton, colors, icons
import math
from components.com_appContainer import AppContainer

class ItemList:
    """
    Classe para exibir uma lista de categorias e itens com funcionalidades de contagem e salvamento.

    Esta classe renderiza categorias em um layout expansível, onde cada item da categoria possui 
    botões de incremento, decremento e um botão para salvar os dados.

    Atributos:
        data (list[dict]): Lista estruturada contendo categorias e itens associados.
            Formato esperado:
            [
                {"Categoria1": {"item1": valor1, "item2": valor2}},
                {"Categoria2": {"item3": valor3, "item4": valor4}},
            ]
        save_callback (function): Callback chamado ao salvar dados de um item.
        bg_color (str): Cor de fundo dos itens.
        color_increment_btn (str): Cor do botão de incremento.
        color_decrement_btn (str): Cor do botão de decremento.
    """

    def __init__(self, data: list[dict], save_callback, page):
        
        """
        Inicializa a classe com os dados e configurações.

        Args:
            data (list[dict]): Lista contendo categorias e itens.
            save_callback (function): Callback para salvar os dados de um item.
        """
        self.page=page
        self.data = data
        self.save_callback = save_callback
        self.bg_color = "#336699"
        self.color_increment_btn = colors.GREEN
        self.color_decrement_btn = "#F93319"
        self.base=AppContainer(self.page)
        
    def build_item_row(self, item_name, item_value):
        """
        Constrói uma linha de item com nome, valor, contador e botões de controle.

        Args:
            item_name (str): Nome do item.
            item_value (float): Valor do item.

        Returns:
            Row: Componente visual contendo os controles do item.
        """
        count = 0
        counter_text = Text(str(count), color="white")

        def increment(e):
            """Incrementa o contador do item."""
            nonlocal count
            count += 1
            counter_text.value = str(count)
            counter_text.update()

        def decrement(e):
            """Decrementa o contador do item (não permite valores negativos)."""
            nonlocal count
            if count > 0:
                count -= 1
            counter_text.value = str(count)
            counter_text.update()

        def save(e):
            """Chama o callback de salvar passando o nome, valor e contador do item."""
            if count != 0:
                self.save_callback(item_name, item_value, count)
                self.base.mensagens_dialog(f"{item_name} adicionado com Sucesso!!!", "success")
            else:
                self.base.mensagens_dialog("Adicione uma quantidade DIFERENTE de 0 !!!", "alert" )

        return ft.Container(
            content=Row(
                controls=[
                    Text(item_name, expand=1, color="white"),
                    Text(f"R$ {item_value:.2f}", expand=1, color="white"),
                    IconButton(icons.REMOVE, on_click=decrement, bgcolor=self.color_decrement_btn, icon_size=20, width=30, opacity=0.5),
                    counter_text,
                    IconButton(icons.ADD, on_click=increment, bgcolor=self.color_increment_btn, icon_size=20, width=30, opacity=0.5),
                    ElevatedButton("Salvar", on_click=save, bgcolor="#0838B2", color=colors.WHITE),
                ]
            ),
        )

    def build_category(self, category_name, items):
        """
        Constrói o componente visual de uma categoria e seus itens.

        Args:
            category_name (str): Nome da categoria.
            items (dict): Dicionário contendo os itens da categoria com seus valores.

        Returns:
            Container: Componente visual representando a categoria.
        """
        controls = [
            Container(
                content=self.build_item_row(item_name, item_value),
                bgcolor=self.bg_color,
                padding=5,
                margin=5,
                border_radius=5,
            )
            for item_name, item_value in items.items()
        ]

        return Container(
            content=ExpansionTile(
                title=Text(category_name, weight=ft.FontWeight.BOLD, font_family="Roboto"),
                controls=controls,
                text_color="white",
                collapsed_text_color="#FFFFFF",
                bgcolor="#0838B2",
                icon_color="white",
                
            ),
            border_radius=20,
            margin=10,
            shadow=ft.BoxShadow(
                spread_radius=0.5,
                blur_radius=15,
                color="#220624",
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
                ),
            gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.Alignment(0.8, 1),
                    colors=[
                        "0xff1f005c",
                        "0xff5b0060",
                        "0xff870160",
                        "0xffac255e",
                        "0xffca485c",
                        "0xffe16b5c",
                        "0xfff39060",
                        "0xffffb56b",
                    ],
                    tile_mode=ft.GradientTileMode.MIRROR,
                    rotation=math.pi / 3,   
                ),


        )

    def render(self):
        """
        Renderiza todas as categorias e seus itens.

        Returns:
            list: Lista de componentes visuais de categorias.
        """
        return [
            self.build_category(category_name, items)
            for category in self.data
            for category_name, items in category.items()
        ]


# Exemplo de uso
data = [
    {"A": {"aaa": 10, "aab": 12, "aac": 1}},
    {"B": {"bbb": 8, "bba": 7, "bbc": 7}},
]

