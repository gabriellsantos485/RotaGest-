from flet import Container, colors, Alignment, FontWeight, Text, Row, MainAxisAlignment, IconButton, Icons
from config.constant import SCREEN_HEIGHT, SCREEN_WIDTH

class TitlesView:
    def __init__(self, page):
        self._wh = SCREEN_WIDTH*0.85
        self._hg= 45
        self.__color =" #5E1680"
        self.__bgcolor = colors.WHITE
        self.__sizeof_text = 35
        self.page = page
        
    def build(self, title):
        
        return Container(
            content=Row(
                controls=[
                    Text(
                            value=title, 
                            size=self.__sizeof_text, 
                            text_align="center", 
                            weight=FontWeight.BOLD,  
                            color=self.__color,                        
                        ),
                    IconButton(
                        icon=Icons.ARROW_BACK,
                        on_click=self.__navegation,
                        
                    )
                    ],
                alignment=MainAxisAlignment.SPACE_BETWEEN, 
            ),
            width=self._wh,
            height=self._hg,
            bgcolor=self.__bgcolor,
            margin=10,
            border_radius=10,
            
        )
        
    def __navegation(self, e):
        """
        Realiza a navegação para a rota especificada quando o botão é clicado.

        Args:
            e: Dados do evento fornecidos pelo framework Flet.
        """
        self.page.go("/")
        
                
                    
        