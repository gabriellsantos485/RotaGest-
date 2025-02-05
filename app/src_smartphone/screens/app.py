import flet as ft
from config.constant import BACKGROUND_IMAGE, APP_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, FONT
        
class AppConfigurator:
    
    @staticmethod
    def configure_page(page: ft.Page):
        """Apply global configurations to the page."""
        page.window_width=405
        page.window_heigh=SCREEN_HEIGHT
        page.window_resizable=False
        page.vertical_alignment=ft.MainAxisAlignment.CENTER
        page.horizontal_alignment=ft.CrossAxisAlignment.CENTER  
        page.title = APP_TITLE
        page.theme=ft.Theme(font_family=FONT)
        return page 
        
    