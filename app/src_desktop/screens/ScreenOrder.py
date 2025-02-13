import flet as ft
from components.BasePage import BasePage
from components.titles_of_pages import TitlesView
from components.TableView import TableView
from services.APIClient import APIClient
from utils.gets import obter_nome_por_id, formatar_data_para_brasil

# Cabeçalhos da tabela
cabecalhos = ["Nome", "Comanda", "N° do Pedido", "Valor Total", "Data"]

class ScreenOrder(BasePage):
    def __init__(self, page: ft.Page)-> None:
        super().__init__(page)
        self.page = page

        # Obtém os dados da API
        self._pedido = APIClient().get_api("http://127.0.0.1:8000/api/pedidos/")

        # Componentes principais
        self.title = TitlesView(page)
        self.list = TableView(cabecalhos=cabecalhos, page=page)

        # Processa os dados da API para exibição na tabela
        dados_formatados = self.__format_data(self._pedido)
        self.list.set_dados(dados_formatados)

    def __format_data(self, pedidos) -> list:
        """
        Formata os dados recebidos da API para serem exibidos na tabela.
        Substitui o ID do cliente pelo nome do cliente usando a função obter_nome_por_id
        e formata a data no padrão brasileiro.
        
        :param pedidos: Lista de dicionários retornada pela API.
        :return: Lista formatada para a tabela.
        """
        if not pedidos or not isinstance(pedidos, list):
            return []  # Retorna uma lista vazia se os dados forem inválidos

        dados_formatados = []
        for pedido in pedidos:
            # Obtém o nome do cliente pelo ID
            cliente_id = pedido.get("cli_id", "N/A")
            nome_cliente_res = obter_nome_por_id(cliente_id)

            # Verifica se a resposta contém o nome ou um erro
            nome_cliente = (
                nome_cliente_res.get("nome", "N/A")
                if "nome" in nome_cliente_res
                else nome_cliente_res.get("error", "Erro ao buscar nome")
            )

            # Formata a data no padrão brasileiro
            data_abertura = pedido.get("ped_abertura", "N/A")
            data_abertura = pedido.get("ped_abertura")  # Pode retornar None
            if data_abertura:  # Verifica se a data não é None
                try:
                    data_formatada = formatar_data_para_brasil(data_abertura)
                except ValueError:  # Caso a data seja inválida
                    data_formatada = "Data inválida"
            else:
                data_formatada = "N/A"

            # Adiciona os dados formatados na lista
            dados_formatados.append({
                "Nome": nome_cliente,
                "Comanda": pedido.get("com_id", "N/A"),
                "N° do Pedido": pedido.get("ped_id", "N/A"),
                "Valor Total": pedido.get("ped_valorTotal", "N/A"),
                "Data": data_formatada,
            })
            
        return dados_formatados

    def content(self) -> ft.Container:
        """
        Constrói o layout da página.
        """
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[self.title.build("Pedidos")],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls=[self.list.build()],
                    ),
                ],
                scroll=True,
            )
        )
        
    def buildMenu(self) -> callable:
        """Builds the menu"""
        return self.build()
