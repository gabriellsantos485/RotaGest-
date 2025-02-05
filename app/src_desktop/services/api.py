import requests
from components.com_appContainer import AppContainer

class Api:
    
    def __init__(self, page):
        self.app = AppContainer(page)
    
    def cadastrar_categoria(self, nome):
        data = {'cat_nome': nome}
        app_container = self.app

        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/categorias/criar_categoria/",
                json=data,
            )
            if response.status_code == 201:
                app_container.show_message("Categoria cadastrada com sucesso!", "green")
            elif response.status_code == 400:
                app_container.show_message("Erro: Categoria já existente. Tente outro nome!", "orange")
            else:
                app_container.show_message(
                    f"Erro inesperado: {response.status_code}", "red"
                )
        except requests.exceptions.ConnectionError:
            app_container.show_message("Erro: Sem acesso ao servidor.", "red")
        except Exception:
            app_container.show_message("Erro: Algo deu errado, tente novamente.", "red")

    
    def get_api(self, url):
        response = requests.get(url)
        return response.json()
    
    def _get_id_categoria(self, nome):
        for i in self.get_api("http://127.0.0.1:8000/api/categorias/"):
            if i['cat_nome'] == nome:
                return i["cat_id"]
            
    def set_api(self, data):
        try:
            response = requests.post("http://127.0.0.1:8000/api/menus/", json=data)
            
            if response.status_code == 201:
                self.app.show_message("Categoria cadastrada com sucesso!", "green")
            else:
                print("Erro na resposta:", response.status_code, response.json())
                self.app.show_message("Erro ao cadastrar o menu.", "red")

        except requests.exceptions.ConnectionError:
            self.app.show_message("Erro: Sem acesso ao servidor.", "red")
        except Exception as e:
            print("Erro desconhecido:", e)
            self.app.show_message("Erro: Algo deu errado, tente novamente.", "red")
            
    def remove(self, url):
        url = url
        try:
            response = requests.delete(url)
            if response.status_code == 200:
                self.app.show_message( "Item apagado com sucesso", "green")
            elif response.status_code == 404:
                self.app.show_message("Não foi possivel deletar o item. Tente novamente!", "red")
            else:
                self.app.show_message(f"Erro inesperado: {response.status_code}, {response.text}")
        except requests.exceptions.RequestException as e:
            self.app.show_message(f"Erro ao conectar ao servidor: {e}")
            
    import requests

    def update(self, data):
        """
        Atualiza um item no banco de dados por meio da API.

        Args:
            data (dict): Dicionário contendo os dados do item a ser atualizado.
                        Deve incluir o 'menu_id' para identificar o item e os novos valores.
        """
        item_id = data.get("menu_id")
        if not item_id:
            print("Erro: O 'menu_id' é necessário para atualizar o item.")
            return

        try:
            # URL da API para o item específico
            url = f"http://127.0.0.1:8000/api/menus/{item_id}/"
            
            # Enviar os dados para atualização
            response = requests.put(url, json=data)
            
            if response.status_code == 200:
                self.app.show_message(f"Item com ID {item_id} atualizado com sucesso.", "green")
            else:
                error_message = response.json().get("detail", "Erro desconhecido.")
                self.app.show_message(f"Erro ao atualizar o item: {error_message}", "red")

        except requests.exceptions.RequestException as e:
            print(f"Erro ao conectar à API: {e}")
            self.app.show_message("Erro ao conectar ao servidor. Tente novamente mais tarde.", "red")


            
        
                
            
