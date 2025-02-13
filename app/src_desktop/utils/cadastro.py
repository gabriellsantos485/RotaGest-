import requests
from components.BasePage import BasePage

def cadastrar_categoria(nome, page):
    data = {'cat_nome': nome}
    app_container = AppContainer(page)

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
