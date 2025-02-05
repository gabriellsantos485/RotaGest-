import flet as ft
from components.com_appContainer import AppContainer
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT
from components.navbar import CustomNavBar
from components.bag_datas import BagData
from context.contextglobals import VarGlobals
from services.api import Api
from services.controler import Controller


class BagScreen():
    def __init__(self, page):
        self.page=page
        self.base = AppContainer(page)
        self.text="Sacola"
        self.color=ft.colors.WHITE
        self.bgcolor_container="#3505A4"
        self.text_size=28
        self.navbar=CustomNavBar(self.page)
        self.globals=VarGlobals()
        self.list=self.globals.get_list()
        self.api=Api()
        self.controler=Controller(api=self.api, app=self.base, globals_context= self.globals)
    
    def get_widget(self):
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Text(
                                    text_align="center",
                                    value=self.text, 
                                    color=self.color,
                                    weight=ft.FontWeight,  
                                    size=self.text_size                          
                                ),
                            ], alignment=ft.MainAxisAlignment.CENTER
                        ),
                        bgcolor=self.bgcolor_container,
                        height=SCREEN_HEIGHT *0.10,
                    ),
                    
                    ft.Container(
                        bgcolor="",
                        width=SCREEN_WIDTH *1,
                        height=SCREEN_HEIGHT * 0.80,
                        padding=10,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            controls=[
                                BagData(self.page, self.list).render(),
                                ft.Container(
                                    content=ft.ElevatedButton(
                                        text="Enviar",
                                        bgcolor=ft.colors.GREEN,
                                        on_click=self.controler.send_data,
                                        width=180,
                                        height=40
                                    ),  
                                    alignment=ft.alignment.center
                                ),
                            ]
                        )
                    ),
                    ft.Container(
                        content=ft.Column(
                                controls=[self.navbar.render()]
                            ),
                        height=SCREEN_HEIGHT*0.10
                    )
                ]
            ),
            
            
        )
        
        return self.base.build(content)
    
    def set_text(self, text):
        self.text = text
        return self.text

    def set_size_text(self, value):
        self.text_size =value
        self.text_size
        
    def set_color_of_text(self, color):
        self.color=color
        return self.color
        
    
    
        
    
        
        


            
        
        