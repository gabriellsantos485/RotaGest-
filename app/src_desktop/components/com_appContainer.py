import flet as ft
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR


class AppContainer:
    def __init__(self, page: ft.Page):
        """
        Initializes the base screen with a global configuration.

        Args:
            page (ft.Page): The main page object.
        """
        self.page = page
        self.__width = SCREEN_WIDTH
        self.__height = SCREEN_HEIGHT
        self.__bgcolor = BACKGROUND_COLOR

    def build(self, content: ft.Control) -> ft.Container:
        """
        Builds the base container with the background image and provided content.

        Args:
            content (ft.Control): The dynamic content to display over the background.

        Returns:
            ft.Container: The configured container with the background and content.
        """
        return ft.Container(
            width=self.__width,
            height=self.__height,
            bgcolor=self.__bgcolor,
            border_radius=20,
            content=ft.Stack(
                controls=[content],  # Dynamic content on top of the background
            ),
            expand=True,
        )

    def center_content(self, container: ft.Container) -> ft.Container:
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
    def mensagens_dialog(self, mensagem: str, tipo: str = "info", conf: bool = False, on_confirm: callable = None):
        """
        Displays a message in a modal dialog with optional confirmation.
        
        Args:
            mensagem (str): The message to display.
            tipo (str): The type of message, e.g., "info", "error", "success", "alert".
            conf (bool): If True, shows confirmation buttons. Defaults to False.
            on_confirm (callable): Function to execute when "Confirmar" is clicked.
        """
        color_font = "white"
        if tipo == "info":
            bg_color = ft.colors.BLUE
        elif tipo == "success":
            bg_color = ft.colors.GREEN
        elif tipo == "error":
            bg_color = ft.colors.RED
        elif tipo == "alert":
            bg_color = ft.colors.YELLOW
            color_font = "black"
        else:
            bg_color = ft.colors.GREY

        # Variável para armazenar o valor do campo de senha
        senha_field = ft.TextField(label="Senha", width=150, height=40, password=True)

        # Define as ações do diálogo
        if conf:
            actions = [
                senha_field,
                ft.TextButton(
                    "Confirmar",
                    width=150,
                    height=40,
                    on_click=lambda e: self.__handle_password_confirm(senha_field.value, on_confirm),
                ),
                ft.TextButton(
                    "Fechar",
                    on_click=lambda e: self.close_dialog(dialog),
                )
            ]
        else:
            actions = [
                ft.TextButton(
                    "Fechar",
                    on_click=lambda e: self.close_dialog(dialog),
                )
            ]

        # Cria o diálogo
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

        # Exibe o diálogo
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def __handle_password_confirm(self, senha: str, on_confirm: callable):
        """
        Handle the password confirmation logic.

        Args:
            senha (str): The entered password.
            on_confirm (callable): The callback to execute.
        """
        if on_confirm:
            on_confirm(senha)
        self.close_dialog(self.page.dialog)



    def close_dialog(self, dialog: ft.AlertDialog):
        """
        Helper function to close a dialog.

        Args:
            dialog (ft.AlertDialog): The dialog to close.
        """
        dialog.open = False
        self.page.update()

    def execute_and_close(self, dialog: ft.AlertDialog, on_confirm: callable):
        """
        Executes a function and closes the dialog.

        Args:
            dialog (ft.AlertDialog): The dialog to close.
            on_confirm (callable): Function to execute.
        """
        if on_confirm:
            on_confirm()
        self.close_dialog(dialog)


    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_bgcolor(self):
        return self.__bgcolor

    def set_bgcolor(self, bgcolor):
        self.__bgcolor = bgcolor
