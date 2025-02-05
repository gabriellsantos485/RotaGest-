from services.api import Api
from components.com_appContainer import AppContainer
from context.contextglobals import VarGlobals
from datetime import datetime
import logging
import requests

# Configurando o logging
logging.basicConfig(level=logging.INFO)

# Centralizando URLs da API
API_URLS = {
    "create_client": "http://127.0.0.1:8000/api/clientes/adicionar_cliente/",
    "update_command_status": "http://127.0.0.1:8000/api/comandas/{}/atualizar_status/",
    "create_order": "http://127.0.0.1:8000/api/pedidos/",
    "create_menu_item": "http://127.0.0.1:8000/api/itens-menu/"
}


class ClientService:
    def __init__(self, api):
        self.api = api

    def create_client(self, client_name: str) -> int:
        """
        Creates a new client in the API.

        Args:
            client_name (str): Name of the client to create.

        Returns:
            int: ID of the created client, or None if the operation fails.
        """
        data = {"cli_nome": client_name}
        response = requests.post(API_URLS["create_client"], json=data)

        if response.status_code == 201:
            return response.json().get("data", {}).get("cli_id")
        else:
            logging.error(f"Error creating client: {response.status_code} {response.text}")
            return None

class CommandService:
    def __init__(self, api):
        self.api = api

    def update_command_status(self, command_id: int, status: str = 1) -> bool:
        """
        Updates the status of a command.

        Args:
            command_id (int): ID of the command to update.
            status (str): New status for the command.

        Returns:
            bool: True if the operation is successful, False otherwise.
        """
        data = {"com_status": status}
        response = requests.patch(url=f"http://127.0.0.1:8000/api/comandas/{command_id}/atualizar_status/", json=data)
        
        if response.status_code == 200:
            return True
        else:
            logging.error(f"Error updating command status: {response.status_code} {response.text}")
            return False

class OrderService:
    def __init__(self, api):
        self.api = api

    def create_order(self, client_id: int, command_id: int, valueSum) -> int:
        """
        Creates a new order associating a client and a command.

        Args:
            client_id (int): ID of the client.
            command_id (int): ID of the command.

        Returns:
            int: ID of the created order, or None if the operation fails.
        """
        data = {
            "cli_id": client_id,
            "com_id": command_id,
            "ped_abertura": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ped_fechamento": None,
            "ped_valorTotal":valueSum
        }
        response = requests.post( API_URLS["create_order"], json=data)

        if response.status_code == 201:
            return response.json().get("data", {}).get("ped_id")
        else:
            logging.error(f"Error creating order: {response.status_code} {response.text}")
            return None

class MenuItemService:
    def __init__(self, api):
        self.api = api

    def create_menu_item(self, order_id: int, item_data: dict) -> bool:
        """
        Creates a menu item for a specific order.

        Args:
            order_id (int): ID of the order.
            item_data (dict): Data of the menu item to create.

        Returns:
            bool: True if the operation is successful, False otherwise.
        """
        item_data["ped_id"] = order_id

        
        response = requests.post(API_URLS["create_menu_item"], json=item_data)

        if response.status_code == 201:
            logging.info(f"Menu item created successfully: {response.json()}")
            return True
        else:
            logging.error(f"Error creating menu item: {response.status_code} {response.text}")
            return False

class Controller:
    def __init__(self, app: AppContainer, api: Api, globals_context: VarGlobals):
        self.app = app
        self.api = api
        self.globals = globals_context

        # Instantiating services
        self.client_service = ClientService(api)
        self.command_service = CommandService(api)
        self.order_service = OrderService(api)
        self.menu_item_service = MenuItemService(api)

    def send_data(self, event):
        """
        Main method to send client, command, and association data to the API.
        """
        order_items = self.globals.get_list()
        if not order_items:
            self.app.mensagens_dialog("Não existe dados para ser enviados!", "error")
            return

        self.app.mensagens_dialog("Confirme para ENVIAR o pedido!", conf=True)

        client_name = self.globals.get_name()
        command_id = self.globals.get_command()

        client_id = self.client_service.create_client(client_name)
        if not client_id:
            self.app.mensagens_dialog("Erro ao cadastrar o cliente!", "error")
            return

        if not self.command_service.update_command_status(command_id):
            self.app.mensagens_dialog("Erro ao atualizar o status da comanda!", "error")
            return

        list_order_ids=self.api.transformar_nome_em_id(self.globals.get_list())
        
        
        order_id = self.order_service.create_order(client_id, command_id, self.calculate_total_value(list_order_ids))
        if not order_id:
            self.app.mensagens_dialog("Erro ao criar o pedido!", "error")
            return

        
        
        for item in list_order_ids:
            if not self.menu_item_service.create_menu_item(order_id, item):
                self.app.mensagens_dialog("Erro ao adicionar itens ao pedido!", "error")
                return

        self.app.mensagens_dialog("Dados enviados com sucesso!", "info")

    def calculate_total_value(self, items_list):
        """
        Calcula o valor total de uma lista de itens.

        Args:
            items_list (list): Lista de dicionários no formato:
                [{'ime_id': int, 'ime_valorUnitario': float, 'ime_qtde': int, 'ped_id': int, 'menu_id': int}, ...]

        Returns:
            float: O valor total calculado.
        """
        total_value = 0.0

        for item in items_list:
            # Verifica se as chaves necessárias estão presentes no item
            unit_value = item.get("ime_valorUnitario", 0.0)
            quantity = item.get("ime_qtde", 0)

            # Soma o valor total para cada item
            total_value += unit_value * quantity

        return total_value
        