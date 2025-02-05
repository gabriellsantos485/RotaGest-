import flet as ft
from config.constant import APP_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, FONT
        
class AppConfigurator:
    
    @staticmethod
    def configure_page(page: ft.Page):
        """Apply global configurations to the page."""
        page.window_width=SCREEN_WIDTH
        page.window_heigh=100
        page.window_resizable=False 
        page.title = APP_TITLE
        page.theme=ft.Theme(font_family=FONT)
        return page
        