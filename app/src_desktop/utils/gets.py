import requests
from datetime import datetime

def obter_nome_por_id(cliente_id, ):
    """
    Consulta o nome de um cliente pelo ID utilizando a API.
    
    :param cliente_id: ID do cliente.
    :param api_base_url: URL base da API (exemplo: http://127.0.0.1:8000/api).
    :return: Nome do cliente ou mensagem de erro.
    """
    try:
        # Constrói a URL para acessar o cliente pelo ID
        url = f"http://127.0.0.1:8000/api/clientes/get_nome/?id={cliente_id}"
        
        # Faz a requisição GET para a API
        response = requests.get(url)
        
        # Verifica o status da resposta
        if response.status_code == 200:
            # Obtém os dados do cliente
            data = response.json()
            return data
        
        elif response.status_code == 404:
            return {"error": "Cliente não encontrado."}  # Cliente não encontrado
        else:
            return {"error": f"Erro na API: {response.status_code}"}
    except requests.RequestException as e:
        return {"error": f"Erro na requisição: {str(e)}"}  # Erro durante a requisição


from datetime import datetime

def formatar_data_para_brasil(data_iso):
    """
    Converte uma data no formato ISO 8601 para o formato brasileiro.
    
    :param data_iso: String no formato 'YYYY-MM-DDTHH:MM:SSZ' ou semelhante.
    :return: String no formato 'DD/MM/YYYY HH:MM:SS'
    """
    try:
        # Remove o 'Z' caso esteja presente e converte para um objeto datetime
        data_obj = datetime.strptime(data_iso.replace("Z", ""), "%Y-%m-%dT%H:%M:%S")
        # Formata o objeto datetime para o padrão brasileiro
        data_formatada = data_obj.strftime("%d/%m/%Y %H:%M:%S")
        return data_formatada
    except ValueError:
        return "Data no formato inválido."
