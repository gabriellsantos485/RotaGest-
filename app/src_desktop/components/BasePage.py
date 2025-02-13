import flet as ft
from abc import ABC, abstractmethod
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR

class BasePage(ABC):
    def __init__(self, page: ft.Page):
        """
        Initializes the base screen with a global configuration.

        Args:
            page (ft.Page): The main page object.
        """
        self.page = page
        self._width = SCREEN_WIDTH
        self._height = SCREEN_HEIGHT
        self._bgcolor = BACKGROUND_COLOR

    @abstractmethod
    def content(self) -> ft.Control:
        """
        Abstract method to be implemented by child classes.

        Returns:
            ft.Control: The dynamic content to display on the screen.
        """
        raise NotImplementedError("The content method must be implemented in a subclass.")

    def build(self) -> ft.Container:
        """
        Builds the base container with the background image and provided content.

        Returns:
            ft.Container: The configured container with the background and content.
        """
        return ft.Container(
            width=self._width,
            height=self._height,
            bgcolor=self._bgcolor,
            border_radius=20,
            content=ft.Stack(
                controls=[self.content()],
            ),
            expand=True,
        )

    def _center_content(self, container: ft.Container) -> ft.Container:
        """
        Adjusts the given container to center its content on the screen.

        Args:
            container (ft.Container): The container to adjust.

        Returns:
            ft.Container: The updated container with centered content.
        """
        container.content = ft.Row(
            controls=[container.content],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        return container

    def app_mess(self, mensagem: str, tipo: str = "info", conf: bool = False, on_confirm: callable = None) -> None:
        """
        Displays a message in a modal dialog with optional confirmation.
        
        Args:
            mensagem (str): The message to display.
            tipo (str): The type of message, e.g., "info", "error", "success", "alert".
            conf (bool): If True, shows confirmation buttons. Defaults to False.
            on_confirm (callable): Function to execute when "Confirmar" is clicked.
        """
        colors = {
            "info": (ft.colors.BLUE, "white"),
            "success": (ft.colors.GREEN, "white"),
            "error": (ft.colors.RED, "white"),
            "alert": (ft.colors.YELLOW, "black"),
        }
        bg_color, color_font = colors.get(tipo, (ft.colors.GREY, "white"))

        actions = [
            ft.TextButton("Fechar", on_click=lambda e: self.close_dialog(dialog))
        ]
        
        if conf:
            senha_field = ft.TextField(label="Senha", width=150, height=40, password=True)
            actions.insert(0, senha_field)
            actions.insert(1, ft.TextButton("Confirmar", width=150, height=40, 
                on_click=lambda e: self._handle_password_confirm(senha_field.value, on_confirm)))

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Mensagem", weight=ft.FontWeight.BOLD),
            content=ft.Container(
                content=ft.Text(mensagem, color=color_font, weight=ft.FontWeight.BOLD),
                bgcolor=bg_color,
                padding=20,
                border_radius=10,
            ),
            actions=actions,
        )

        self.page.show_dialog(dialog)

    def _handle_password_confirm(self, senha: str, on_confirm: callable) -> None:
        """
        Handle the password confirmation logic.

        Args:
            senha (str): The entered password.
            on_confirm (callable): The callback to execute.
        """
        if on_confirm:
            on_confirm(senha)
        self.close_dialog(self.page.dialog)

    def close_dialog(self, dialog: ft.AlertDialog) -> None:
        """
        Helper function to close a dialog.

        Args:
            dialog (ft.AlertDialog): The dialog to close.
        """
        if dialog:
            dialog.open = False
            self.page.update()
            self.page.dialog = None  # Remove referência para evitar reabertura inesperada

    def execute_and_close(self, dialog: ft.AlertDialog, on_confirm: callable) -> None:
        """
        Executes a function and closes the dialog.

        Args:
            dialog (ft.AlertDialog): The dialog to close.
            on_confirm (callable): Function to execute.
        """
        if on_confirm:
            on_confirm()
        self.close_dialog(dialog)
