import flet as ft  # Importa o módulo Flet
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT  # Importa as constantes de largura e altura da tela


class DynamicContainer:
    """
    Classe que representa o container dinâmico que pode ser atualizado.
    """
    def __init__(self, page: ft.Page, width: int = SCREEN_WIDTH * 0.65, height: int = SCREEN_HEIGHT * 0.85):
        """
        Inicializa a classe com um controle padrão.

        Args:
            page (ft.Page): Página principal da aplicação.
            width (int): Largura do container.
            height (int): Altura do container.
        """
        # Controle inicial padrão
        self._content = ft.Text("Welcome! Click a button to update this content.", size=20)

        # Container configurado
        self.container = ft.Container(
            content=self._content,
            alignment=ft.alignment.center,
            bgcolor="#2C799F",
            border_radius=10,
            padding=20,
            expand=True,
            width=width,
            height=height,
        )

    def update_content(self, new_control: ft.Control):
        """
        Atualiza o conteúdo do container com um novo controle.

        Args:
            new_control (ft.Control): O novo controle a ser exibido no container.
        """
        self.container.content = new_control
        self.container.update()

    def get_container(self) -> ft.Container:
        """
        Retorna o container para ser usado no layout.

        Returns:
            ft.Container: O container dinâmico atualizado.
        """
        return self.container
