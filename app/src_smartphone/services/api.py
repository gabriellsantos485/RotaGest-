import requests

class Api:
    
    def __init__(self):
        pass
    
    def get_api(self, url):
        response = requests.get(url)
        return response.json()
    
    def set_datas_client(self, data, url):
        """
        Envia dados para criar um cliente na API e retorna a resposta da requisição.
        """
        try:
            response = requests.post(url, json=data)
            if response.status_code in [200, 201]:
                return response  # Retorna a resposta para uso posterior
            else:
                print("Erro na resposta:", response.status_code, response.json())
                return None
        except requests.exceptions.ConnectionError:
            print("Erro: Sem acesso ao servidor.")
            return None
        except Exception as e:
            print("Erro desconhecido:", e)
            return None 
            
            
            
    def update_datas_client(self, data, url):
        try:
            response = requests.patch(url, json=data)
            
            # Verificar o código de status
            if response.status_code == 201:
                print("Cadastrado com sucesso!")
            elif response.status_code == 200:
                # Tentar obter detalhes adicionais na resposta
                try:
                    response_data = response.json()
                    print("Resposta recebida:", response_data)
                    
                    # Verificar se contém mensagens de sucesso ou erro no JSON
                    if "error" in response_data:
                        print(f"Mensagem de erro: {response_data['error']}")
                    else:
                        print("Operação aparentemente bem-sucedida, mas verifique os detalhes:", response_data)
                except ValueError:
                    print("Resposta inválida do servidor (não é JSON).")
            else:
                print(f"Erro inesperado: {response.status_code}")
                try:
                    error_message = response.json().get("error", "Erro desconhecido")
                    print(f"Mensagem de erro: {error_message}")
                except ValueError:
                    print("Resposta inválida do servidor (não é JSON).")

        except requests.exceptions.ConnectionError:
            print("Erro: Sem acesso ao servidor.")
        except Exception as e:
            print("Erro desconhecido:", str(e))
            print("Erro: Algo deu errado, tente novamente.")

    
    def transformar_nome_em_id(self, lista_de_itens):
        """
        Transforma a lista de itens substituindo o campo 'name' pelo 'id' correspondente,
        consultando a API para buscar o ID baseado no nome.

        Args:
            lista_de_itens (list): Lista de dicionários no formato:
            [{"name": item_name, "value": item_value, "count": item_count}, ...]

        Returns:
            list: Lista atualizada com 'name' substituído pelo 'id'.
        """
        updated_list = []

        for item in lista_de_itens:
            nome = item.get("name")
            if not nome:
                continue  # Ignora itens sem o campo 'name'

            try:
                # Faz uma consulta na API para obter o ID pelo nome
                response = requests.get(f"http://127.0.0.1:8000/api/menus/buscar_por_nome/?nome={nome}", )
                
                if response.status_code == 200:
                    # Substitui o campo 'name' pelo 'id'
                    updated_item = item.copy()
                    updated_item["menu_id"] = response.json()["id"]
                    updated_item["ime_valorUnitario"] = item['value']
                    updated_item["ime_qtde"] = item["count"]

                    
                    updated_item.pop("name", None)  # Remove o campo 'name'
                    updated_item.pop("value") #remove o campo 'value'
                    updated_item.pop("count") #remove o campo count
                     
                    updated_list.append(updated_item)
 
                else:
                    print(f"Erro na API para o nome {nome}: {response.status_code}")
            except Exception as e:
                print(f"Erro ao consultar API para o nome {nome}: {e}")

        return updated_list

     
            