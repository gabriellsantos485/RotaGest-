from flet import ElevatedButton, IconButton
import flet as ft
from config.constant import SCREEN_WIDTH



#Ever buttons of system
class Button:
    def __init__(self):
        """
        Button -> Renders a button 
        
        name: Button name 
        Color: Button Color 
        Widht: Button width 
        Height: Button height
        """
        self.__name=""
        self.__color="#3A0762"
        self.__widht= SCREEN_WIDTH * 0.40
        self.__height=50
    
    def renderButtonElevate(self, new_onclick) -> ElevatedButton:
        """
        Renders an Elavate-type button without an icon
        """
        return ElevatedButton(
            text=self.__name,
            on_click=new_onclick,
            bgcolor=self.__color,
            width=self.__widht,
            height=self.__height,
            color=ft.colors.WHITE,
        )
    
    def renderButtonIcon(self, onclick, icon : str)-> IconButton: 
        """
        Renders an Icon-Type button
        """
        return IconButton(
            icon=icon,
            on_click=onclick,
            width=self.__widht,
            height=self.__height,
            bgcolor=self.__color,
        )
        
    def set_name(self, new_name : str) -> str:
        self.__name=new_name
        return self.__name
    
    def set_width(self, new_value: int) -> int:
        self.__widht=new_value
        return self.__widht
    
    def set_height(self, new_value: int) -> int:
        self.__height= new_value
        return self.__height
    
    def set_color(self, new_color: ft.colors) -> str:
        self.__color=new_color
        return self.__color
    
    def get_value(self):
        return self.value
    
    
class ButtonCategory(Button): #leva para categoria
    '''
    Description: Button Category is a component of screen Category
    '''
    def __init__(self):
        super().__init__()
        self.__name=self.set_name("Seguir")
    

class ButtonSave(ElevatedButton):
    def __init__(self):
        super().__init__()

class ButtonNavBarHome(IconButton):
    def __init__(self):
        super().__init__()

class ButtonNavBarBag(IconButton):
    def __init__(self):
        super().__init__()

class ButtonNavBarPeople(IconButton):
    def __init__(self):
        super().__init__()
        
class SaveOfOrder(ElevatedButton):
    
    '''
    Description: Update data for API
    '''
    def __init__(self):
        super().__init__()
        
        
        
        