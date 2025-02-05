import flet as ft
from components.com_appContainer import AppContainer


class ClientsScreen:
    def __init__(self, page):
        self.page=page
        self.base=AppContainer(page)
    
    def get_widget(self):
        content=ft.Container(
            content=ft.Column(
                controls=[
                    
                ]
            )
        )
        
        return self.base.build(content)

