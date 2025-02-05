import flet as ft
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE

class AppContainer:
    
    
    def __init__(self, page: ft.Page):
        """
        Initializes the base screen with a global configuration.

        Args:
            page (ft.Page): The main page object.
            background_image (str): URL or file path for the background image.
        """
        self.page = page
        self.background_image = BACKGROUND_IMAGE

    def build(self, content: ft.Control) -> ft.Container:
        """
        Builds the base container with the background image and provided content.

        Args:
            content (ft.Control): The dynamic content to display over the background.

        Returns:
            ft.Container: The configured container with the background and content.
        """
        return ft.Container(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            border_radius=20,
            content=ft.Stack(
                controls=[
                    
                    content,  # Dynamic content on top of the background
                ]
            ),
            expand=True,
            gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,  # Gradiente começa no topo
            end=ft.alignment.bottom_center,  # Termina na parte inferior
            colors=[
                "#0D47A1",  # Azul escuro profundo
                "#1565C0",  # Azul médio vibrante
                "#1E88E5",  # Azul brilhante
                "#64B5F6",  # Azul claro suave
                "#BBDEFB",  # Azul pálido
            ],
            stops=[0, 0.25, 0.5, 0.75, 1],  # Posições das tonalidades ao longo do gradiente
            
        )
        
    )
        
    def mensagens_snackBar(self, mensagem: str, tipo: str = "info"):
        """
        Displays a message on the screen using a Snackbar.

        Args:
            mensagem (str): The message to display.
            tipo (str): The type of message, e.g., "info", "error", "success". Defaults to "info".
        """
        # Define styles for different message types
        if tipo == "info":
            bg_color = ft.colors.BLUE
        elif tipo == "success":
            bg_color = ft.colors.GREEN
        elif tipo == "error":
            bg_color = ft.colors.RED
        else:
            bg_color = ft.colors.GREY

        # Create and show the Snackbar
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(mensagem, color=ft.colors.WHITE),
            bgcolor=bg_color,
        )
        self.page.snack_bar.open = True
        self.page.update()
        
    
    def mensagens_dialog(self, mensagem: str, tipo: str = "info", conf: bool = False, on_confirm: callable = None):
        """
        Displays a message in a modal dialog.

        Args:
            mensagem (str): The message to display.
            tipo (str): The type of message, e.g., "info", "error", "success", "alert". Defaults to "info".
            conf (bool): If True, shows confirmation buttons. Defaults to False.
            on_confirm (callable): Function to execute when "Confirmar" is clicked. Defaults to None.
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

        # Define actions based on confirmation flag
        if conf:
            actions = [
                ft.TextButton(
                    "Confirmar",
                    on_click=lambda e: self.execute_and_close(dialog, on_confirm),
                ),
                ft.TextButton(
                    "Não",
                    on_click=lambda e: self.close_dialog(dialog),
                ),
            ]
        else:
            actions = [
                ft.TextButton(
                    "Fechar",
                    on_click=lambda e: self.close_dialog(dialog),
                )
            ]

        # Create the dialog
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

        # Attach and show the dialog
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

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
