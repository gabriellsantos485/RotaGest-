import flet as ft
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT

class Button:

    def __init__(self, page: ft.Page, route=None):
        self._color = "#063A3E"
        self._width = SCREEN_WIDTH * 0.22 
        self._height = 40  
        self._size_text = 20  
        self.route = route  
        self._page = page    
        self._opacidade=True

    def build(self, text: str) -> ft.ElevatedButton:
        """
        Constrói e retorna um botão estilizado com base nas propriedades definidas.

        Args:
            text (str): Texto exibido no botão.

        Returns:
            ft.ElevatedButton: Instância do botão configurado.
        """
        return ft.ElevatedButton(
            text=text,
            width=self._width,
            height=self._height,
            bgcolor=self._color,  # Cor de fundo do botão
            color=ft.colors.WHITE,  # Cor do texto
            on_click=self.__set_onclick(),  # Método chamado ao clicar no botão
            opacity=self.set_opacidade(),
        )

    def __navegation(self, e):
        """
        Realiza a navegação para a rota especificada quando o botão é clicado.

        Args:
            e: Dados do evento fornecidos pelo framework Flet.
        """
        self._page.go(self.route)

    def _on_click(self, e):
        print("Sem Implementação")

    def set_opacidade(self):
        if self._opacidade == True:
            self._opacidade = 1
            return self._opacidade
            
        else:
            self._opacidade =0.5
            return self._opacidade
        
    def __set_onclick(self):
        if self.route != None:
            return self.__navegation
        else:
            return self._on_click
        
class ButtonControlOrder(Button):
    
    def __init__(self, page):
        super().__init__(page, route="/pedidos")

class ButtonOrdersQueue(Button):
    
    def __init__(self, page):
        super().__init__(page)
        
class ButtonHistory(Button):
    
    def __init__(self, page):
        super().__init__(page)
    

        
         
    