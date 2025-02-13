import requests
import json

# Substitua pelo seu Access Token real
ACCESS_TOKEN = "APP_USR-6108478866214612-021012-43a60b2730aaaf255f4f1f4d9422d4e8-1457509133"

# URL da API para consultar dispositivos vinculados
API_URL = "https://api.mercadopago.com/point/integration-api/devices"

def listar_dispositivos():
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Lança erro se o status não for 2xx

        # 🔹 Debug: Veja o formato da resposta
        print("Resposta da API:", response.text)

        resposta_json = response.json()

        # 🔹 A API retorna um dicionário com a chave "devices", que contém a lista de maquininhas
        dispositivos = resposta_json.get("devices", [])

        if not dispositivos:
            return "Nenhum dispositivo encontrado na conta."

        resultado = "📌 Dispositivos encontrados:\n"
        for dispositivo in dispositivos:
            resultado += f"\n🔹 **Device ID:** {dispositivo.get('id', 'N/A')}\n"
            resultado += f"📌 **POS ID:** {dispositivo.get('pos_id', 'N/A')}\n"
            resultado += f"🏪 **Store ID:** {dispositivo.get('store_id', 'N/A')}\n"
            resultado += f"⚡ **Modo de Operação:** {dispositivo.get('operating_mode', 'N/A')}\n"

        return resultado
    
    except requests.exceptions.HTTPError as http_err:
        return f"❌ Erro HTTP: {http_err}\n🔹 Detalhes: {response.text}"
    except requests.exceptions.RequestException as req_err:
        return f"❌ Erro de conexão: {req_err}"

# 🔹 Teste da função
if __name__ == "__main__":
    resultado = listar_dispositivos()
    print(resultado)
