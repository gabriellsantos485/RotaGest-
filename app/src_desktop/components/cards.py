import flet as ft
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR

class Card:
    def __init__(self, bgcolor, img):
        self._widget=SCREEN_WIDTH*0.24
        self._height=SCREEN_HEIGHT*0.85
        self._bgcolor=bgcolor
        self.__img = img
        self._spacing_btn=20
        

    def build(self, list_btns: list) -> ft.Container:
        # Número de botões por linha
        buttons_per_row = 1

        # Criar linhas dinamicamente
        rows = []
        for i in range(0, len(list_btns), buttons_per_row):
            rows.append(
                ft.Row(
                    controls=list_btns[i:i + buttons_per_row],  # Pega uma fatia da lista de botões
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )

        return ft.Container(
            width=self._widget,
            height=self._height,
            bgcolor=self._bgcolor,
            border_radius=0,
            margin=10,
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        width=self._widget * 0.98,
                        height=SCREEN_HEIGHT * 0.53,
                        content=ft.Image(
                            src=self.__img,
                            fit=ft.ImageFit.COVER,
                        ),
                    ),
                    *rows,  # Adiciona todas as linhas de botões abaixo da imagem
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=self._spacing_btn,  # Espaçamento entre as linhas
            ),
        )

        
    def set_widget(self, widget):
        self._widget = widget
        
    def set_height(self, height):
        self._height = height
        
    def set_bgcolor(self, bgcolor):   
        self._bgcolor = bgcolor
    
    def create_buttons(self, text, color):
        return ft.ElevatedButton(
            text=text,
            bgcolor=color,
            width=100,
            height=50,
            border_radius=10,
            margin=10,
            padding=10,
        )
    
    def set_spacing_btn(self, spacing):
        self._spacing_btn = spacing
        return self._spacing_btn
        
    