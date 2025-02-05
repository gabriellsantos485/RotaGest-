import flet as ft
from components.com_appContainer import AppContainer
from components.texts import TextClient
from components.expansionTile import CategoryList, Category
from context.contextglobals import VarGlobals
from components.listItems import ItemList
from utils.helpers import create_save_callback
from config.constant import SCREEN_HEIGHT, SCREEN_WIDTH
from components.navbar import CustomNavBar
from services.api import Api

def save_callback(name, value, count):
    print(f"Salvando: {name}, Valor: {value}, Quantidade: {count}")
    
class CategoryScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        self.navbar = CustomNavBar(page)
        self.name = TextClient(VarGlobals.get_name(), page)
        self.command = TextClient(VarGlobals.get_command(), page)
        self.base = AppContainer(page)
        self.api = Api()
        self.save_callback = create_save_callback(page)
        self.item_list = ItemList(self.api.get_api("http://127.0.0.1:8000/api/menus/listar_por_categoria/"), self.save_callback, page)

    def get_widget(self):
        content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.TextField(label="Pesquisar...", bgcolor=ft.colors.WHITE, width=300, height=40, border_radius=10, )
                                        ]),
                                    margin=10
                                ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.IconButton(icon=ft.icons.SEARCH, bgcolor="#3A0762", icon_color="white", opacity=0.6)
                                    ]
                                ),
                                margin=10
                            )
                            
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        width=SCREEN_WIDTH * 0.98,
                        height=SCREEN_HEIGHT * 0.10,
                    ),
                    # Substituir o conteúdo do Container no layout por:
                    

                    ft.Container(
                        content=ft.Column(
                            controls=self.item_list.render(),
                            scroll="auto",
                            width=SCREEN_WIDTH * 0.95,
                            height=SCREEN_HEIGHT * 0.80,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        padding=10,
                        #bgcolor="#CE7D7D",
                        width=SCREEN_WIDTH * 0.95,
                        height=SCREEN_HEIGHT * 0.80,
                    ),
                    
                    ft.Container(
                        content=ft.Column(
                            controls=[self.navbar.render()],
                            width=SCREEN_WIDTH,
                            height=SCREEN_HEIGHT * 0.10,
                        ),
                    ),
                ],
            ),
        )

        return self.base.build(content)
