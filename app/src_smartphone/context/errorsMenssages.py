import flet as ft

class ErrorMessages:
    """
    Classe que centraliza mensagens de erro para a aplicação.
    """

    @staticmethod
    def page_not_found():
        return "A página solicitada não foi encontrada. Verifique a URL e tente novamente."

    @staticmethod
    def invalid_input():
        return "Entrada inválida. Por favor, corrija os dados fornecidos e tente novamente."

    @staticmethod
    def server_error():
        return "Erro no servidor. Por favor, tente novamente mais tarde."

    @staticmethod
    def unauthorized_access():
        return "Acesso não autorizado. Verifique suas credenciais ou entre em contato com o suporte."

    @staticmethod
    def unknown_error():
        return "Ocorreu um erro desconhecido. Por favor, entre em contato com o suporte técnico."

