from flet import TextField
from config.constant import SCREEN_WIDTH
import flet as ft

class Field:
    
    def __init__(self, name, bgcolor):
        """
        Fields -> Typing fields 
        
        text: name that will be in the
        Color: Field Color
        width: width of the field
        height: height of the field
        font: writing font 
        Border: border_radius of the field
        size: font size 
        """
        self.__text=ft.Text(value=name, font_family="Open Sans")
        self.__bgcolor=bgcolor
        self.__width=SCREEN_WIDTH * 0.98
        self.__size=14
        self.__border=20
        self.__height=60
        self.font=None
        
        self.__textfield = ft.TextField(
            text_size=self.__size,
            label=self.__text,
            bgcolor=self.__bgcolor,
            width=self.__width,
            height=60,
            border_radius=20,
            color=ft.colors.BLACK,
            
        )
        
    def render(self) -> TextField:
        """
        Render -> Field Rendering
        """
        return self.__textfield
        
    def get_value(self):
        return self.__textfield.value
    
    def get_text(self) -> str:
        return self.__text
    
    def get_width(self) -> int:
        return self.__width
    
    def get_height(self) -> int:
        return self.__height
    
    def get_border_radius(self) -> int:
        return self.__border
    
    def set_text(self, text : str) -> ft.Text:
        self.__text=text
        return self.__text
    
    def set_width(self, wd : int) -> ft.Control:
        self.__width = wd
        return self.__width
    
    def set_height(self, hg : int) -> ft.Control:
        self.__height= hg
        return hg
    
    def set_border_raidus(self, value : int) -> ft.BorderRadius:
        self.__border = value
        return self.__border
    
    def set_font(self, font : str) ->str:
        self.font = font
        return self.font
    
    def set_color(self, color : str) -> ft.colors:
        self.__color=color
        return self.__color
    
    
class ComandName(Field):
    
    def __init__(self):
        super().__init__(name="Nome", bgcolor="#E6F2F1")

     
        
class ComandNumber(Field):
    
    def __init__(self):
        super().__init__(name="Comanda", bgcolor="#E6F2F1")
        