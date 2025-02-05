import flet as ft
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT

class Button:
    """
    Classe personalizada para criar um botão estilizado em uma aplicação Flet.

    Atributos:
        _color (str): Cor de fundo do botão.
        _width (int): Largura do botão em pixels.
        _height (int): Altura do botão em pixels.
        _size_text (int): Tamanho da fonte do texto do botão (padrão é 20).
        route (str): Rota para a qual o botão navegará ao ser clicado.
        page (ft.Page): Instância da página Flet responsável por lidar com a navegação.

    Métodos:
        build(text: str) -> ft.ElevatedButton:
            Constrói e retorna um botão estilizado (ElevatedButton) com as propriedades definidas.
        
        __navegation(e):
            Lida com a navegação para a rota especificada quando o botão é clicado.

        set_onclick(onclick):
            Define uma função personalizada a ser chamada quando o botão é clicado.

        set_color(new_color):
            Atualiza a cor de fundo do botão.
    """

    def __init__(
        self, page: ft.Page, 
        route=None, color: str = "#063A3E", 
        width=SCREEN_WIDTH * 0.22, 
        height=40, opacidade=True,
        ):
        """
        Inicializa uma instância da classe Button com as propriedades especificadas.

        Args:
            page (ft.Page): Instância da página Flet para lidar com a navegação.
            route (str): Rota para a qual o botão navegará (padrão é None).
            color (str): Cor de fundo do botão (padrão é "#063A3E").
        """
        self._color = color
        self._width = width  # Define a largura do botão proporcional à largura da tela
        self._height = height  # Altura fixa do botão
        self._size_text = 20  # Tamanho padrão da fonte do texto
        self.route = route  # Define a rota de navegação
        self.page = page  # Instância da página para lidar com eventos
        self._onclick = self.__navegation  # Método padrão de clique é a navegação
        self._opacidade=opacidade

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
            color="white",  # Cor do texto
            on_click=self._onclick,  # Método chamado ao clicar no botão
            opacity=self.set_opacidade(),
        )

    def __navegation(self, e):
        """
        Realiza a navegação para a rota especificada quando o botão é clicado.

        Args:
            e: Dados do evento fornecidos pelo framework Flet.
        """
        self.page.go(self.route)

    def set_onclick(self, onclick):
        """
        Define uma função personalizada para ser chamada quando o botão for clicado.

        Args:
            onclick (function): Função a ser executada no evento de clique.
        """
        self._onclick = onclick

    def set_color(self, new_color):
        """
        Atualiza a cor de fundo do botão.

        Args:
            new_color (str): Nova cor de fundo do botão (em formato hexadecimal).
        """
        self._color = new_color

    def set_width(self, new_width):
        self._width = new_width
        
    def set_height(self, new_height):
        self._height = new_height
        
    def set_opacidade(self):
        if self._opacidade == True:
            self._opacidade = 1
            return self._opacidade
            
        else:
            self._opacidade =0.5
            return self._opacidade