import flet as ft
from config.constant import SCREEN_WIDTH


class Text:
    
    def __init__(self, text, page : ft.Page):
        self.text=text
        self.__width=SCREEN_WIDTH * 0.38
        self.__height=60
        self.page=page
        
        self.txt = ft.Text(
            value=str.capitalize(self.text),
            width=self.__width,
            height=self.__height,
            size=24,
            text_align='center',
            color=ft.colors.WHITE
        )
        
    def renderText(self):
        return self.txt
        

class TextClient(Text):
    
    def __init__(self, var, page):
        super().__init__(text=var, page=page)
    



