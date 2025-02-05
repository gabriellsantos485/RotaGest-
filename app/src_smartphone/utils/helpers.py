# utils.py
import flet as ft
from context.contextglobals import VarGlobals
from components.com_appContainer import AppContainer
from components.mensages import SnackbarMessage

def create_save_callback(page):
    """
    Salvar pedidos dos clientes em uma lista global 
    
    Usado em scr_category
    """
    
    def save_item(name, value, count):
        """
        name: str - o nome do item 
        count: str - a quantidade de itens
        """
        # Adiciona o item e quantidade à lista global
        VarGlobals.set_list(name, value, count) 
        
    return save_item
    
    
def clientName():
    VarGlobals().get_name()