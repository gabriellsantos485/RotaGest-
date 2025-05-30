import logging
import requests

"""
 Abstração dos comando da api 
"""

# Configuração do logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Salva logs em um arquivo
        logging.StreamHandler()  # Exibe logs no console
    ]
)

logger = logging.getLogger(__name__)

class APIClient:
    
    def register_data(self, name, url) -> str:
        data = {'cat_nome': name}
        
        try:
            response = requests.post(
                url, 
                json=data,
            )
            if response.status_code == 201:
                return True
            elif response.status_code == 400:
                logger.warning("Erro: Categoria já existente. Tente outro nome!")
            else:
                logger.error(f"Erro inesperado: {response.status_code}")
        except requests.exceptions.ConnectionError:
            logger.critical("Erro: Sem acesso ao servidor.")
        except Exception as e:
            logger.exception("Erro: Algo deu errado, tente novamente.")
    
    def get_api(self, url) -> dict:
        response = requests.get(url)
        return response.json()
    
    def casting_to_id(self, iten: str, column_name : str, url :str, column_id: str) -> int:
        for i in self.get_api(url):
            if i[column_name] == iten:
                return i[column_id]
            
    def set_data(self, data) -> bool:
        try:
            response = requests.post("http://127.0.0.1:8000/api/menus/", json=data)
            
            if response.status_code == 201:
                return True
            else:
                logger.error(f"Erro na resposta: {response.status_code}, {response.json()}")
        except requests.exceptions.ConnectionError:
            logger.critical("Erro: Sem acesso ao servidor.")
        except Exception as e:
            logger.exception("Erro desconhecido ao cadastrar o menu.")
            
    def remove(self, url) -> bool:
        try:
            response = requests.delete(url)
            if response.status_code == 200:
                return True
            elif response.status_code == 404:
                logger.warning("Não foi possível deletar o item. Tente novamente!")
            else:
                logger.error(f"Erro inesperado: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            logger.exception(f"Erro ao conectar ao servidor: {e}")
            
    def update(self, data, url) -> None:
        item_id = data.get("menu_id")
        if not item_id:
            logger.error("Erro: O 'menu_id' é necessário para atualizar o item.")
            return
        
        try:
            response = requests.put(url, json=data)
            
            if response.status_code == 200:
                logger.info(f"ID {item_id} atualizado com sucesso.")
                return True
            else:
                error_message = response.json().get("detail", "Erro desconhecido.")
                logger.error(f"Erro ao atualizar o item: {error_message}")
        except requests.exceptions.RequestException as e:
            logger.exception(f"Erro ao conectar à API: {e}")
            
    def update_pedido_status(self, pedido_id: int, novo_status: str) -> bool:
        """
        Atualiza o status de um pedido específico.

        Args:
            pedido_id (int): ID do pedido a ser atualizado.
            novo_status (str): Novo status do pedido.

        Returns:
            bool: True se a atualização for bem-sucedida, False caso contrário.
        """
        url = f"http://127.0.0.1:8000/api/pedidos/{pedido_id}/"
        data = {"ped_status": novo_status}

        try:
            response = requests.patch(url, json=data)
            
            if response.status_code == 200:
                logger.info(f"Pedido {pedido_id} atualizado para status '{novo_status}'.")
                return True
            else:
                logger.error(f"Erro ao atualizar pedido {pedido_id}: {response.json()}")
                return False
        except requests.exceptions.RequestException as e:
            logger.exception(f"Erro ao conectar à API: {e}")
            return False

