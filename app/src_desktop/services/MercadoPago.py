import requests
import json

# 🔹 Configurações
ACCESS_TOKEN = "APP_USR-6108478866214612-021012-43a60b2730aaaf255f4f1f4d9422d4e8-1457509133"
DEVICE_ID = "PAX_A910__SMARTPOS1493994603"  # Obtido via API

# 🔹 URLs da API do Mercado Pago
API_URL_INTENT = f"https://api.mercadopago.com/point/integration-api/devices/{DEVICE_ID}/payment-intents"

# 🔹 Função para verificar e cancelar pagamento pendente
def cancelar_pagamento_pendente():
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    try:
        # 🔹 Verifica se há uma intenção ativa
        response = requests.get(API_URL_INTENT, headers=headers)
        response.raise_for_status()
        intent_data = response.json()

        # 🔹 Se houver uma intenção, cancela
        if intent_data.get("status") in ["OPEN", "PENDING"]:
            print(f"⚠️ Cancelando pagamento pendente: {intent_data.get('id')}")
            cancel_response = requests.delete(API_URL_INTENT, headers=headers)
            cancel_response.raise_for_status()
            print("✅ Pagamento pendente cancelado com sucesso!")

    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao verificar/cancelar pagamento: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Erro de conexão: {req_err}")

# 🔹 Função para enviar pagamento para a maquininha
def pay_buy(valor, metodo_pagamento="credit_card"):
    cancelar_pagamento_pendente()  # Garante que não há pendências antes de criar um novo pagamento

    payload = {
        "amount": valor,
        
    }

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(API_URL_INTENT, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return f"✅ Pagamento enviado com sucesso!\n🔹 Payment Intent ID: {data.get('id')}\n⚡ Status: {data.get('status')}"

    except requests.exceptions.HTTPError as http_err:
        return f"❌ Erro HTTP: {http_err}\n🔹 Detalhes: {response.text}"
    except requests.exceptions.RequestException as req_err:
        return f"❌ Erro de conexão: {req_err}"

# 🔹 Teste da função
if __name__ == "__main__":
    valor_pagamento = 158.00
    metodo_pagamento = "credit_card"
    resultado = pay_buy(valor_pagamento, metodo_pagamento)
    print(resultado)
