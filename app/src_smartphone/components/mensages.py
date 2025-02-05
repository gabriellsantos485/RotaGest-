

class SnackbarMessage:
    """
    Implementação concreta da exibição de mensagens usando Snackbar.
    """
    def __init__(self, page):
        """
        Inicializa a mensagem Snackbar.

        Args:
            page: Instância da página ou contexto do framework.
        """
        self.page = page

    def show_message(self, message: str):
        """
        Exibe a mensagem no formato de Snackbar.

        Args:
            message (str): A mensagem a ser exibida.
        """
        snackbar = self.page.snack_bar
        if not snackbar:
            from flet import SnackBar, Text
            snackbar = SnackBar(content=Text(message))
            self.page.snack_bar = snackbar
        
        snackbar.content.value = message
        snackbar.open = True
        self.page.update()
