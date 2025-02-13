import flet as ft
from services.APIClient import APIClient


class Barra:
    """
    Classe responsável por gerar uma barra de cardápio dinâmica baseada em uma lista de itens.
    """

    def __init__(self, lista: list, page, on_remove=None):
        """
        Inicializa a Barra.

        Args:
            lista (list): Lista de itens a ser exibida.
            page: Página principal da aplicação.
            on_remove (callable): Função a ser chamada ao remover um item.
        """
        self.lista = lista  # Lista de itens a ser exibida
        self.page = page  # Página principal
        self.api = APIClient()  # Objeto para comunicação com a API
        self.on_remove = on_remove  # Função de callback para remoção de itens

    def remover_item(self, item_id):
        """
        Método para remover um item. Chama o callback `on_remove`, se fornecido.

        Args:
            item_id: ID do item a ser removido.
        """
        if self.on_remove:
            self.on_remove(item_id)  # Chama a função de callback passando o ID do item

    def salvar_edicao(self, item_id, nome_ref, valor_ref):
        """
        Salva os dados editados usando a API.

        Args:
            item_id: ID do item a ser atualizado.
            nome_ref: Referência para o campo de nome.
            valor_ref: Referência para o campo de valor.
        """
        nome = nome_ref.current.value
        valor = valor_ref.current.value

        # Remove o "R$" e converte o valor para float
        valor = float(valor.replace("R$", "").strip()) if valor.startswith("R$") else float(valor)
        data = {
            "menu_id": item_id,
            "menu_nome": nome,
            "menu_valor": valor,
        }
        self.api.update(data)

    def build(self) -> ft.Column:
        """
        Constrói o layout dinâmico do cardápio.

        Returns:
            ft.Column: Uma coluna contendo os cabeçalhos e as linhas dos itens.
        """
        rows = []

        for item in self.lista:
            # Cria referências para os campos de entrada
            nome_ref = ft.Ref[ft.TextField]()
            valor_ref = ft.Ref[ft.TextField]()

            row = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(str(item.get("menu_id", "")), width=50, size=16, color="white"),
                        ft.TextField(
                            value=item.get("menu_nome", ""),
                            expand=1,
                            color="white",
                            text_align=ft.TextAlign.START,
                            ref=nome_ref,  # Referência para capturar o valor do campo de nome
                        ),
                        ft.TextField(
                            value=f'R$ {item.get("menu_valor", 0):.2f}',
                            width=100,
                            color="white",
                            ref=valor_ref,  # Referência para capturar o valor do campo de valor
                        ),
                        ft.IconButton(
                            icon=ft.icons.SAVE,
                            icon_color="white",
                            bgcolor="blue",
                            height=37,
                            icon_size=20,
                            on_click=lambda e, item=item, nome_ref=nome_ref, valor_ref=valor_ref: self.salvar_edicao(
                                item_id=item["menu_id"], nome_ref=nome_ref, valor_ref=valor_ref
                            ),  # Função para salvar a edição
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE_OUTLINE,
                            icon_color="white",
                            bgcolor="red",
                            height=37,
                            icon_size=22,
                            on_click=lambda e, item_id=item["menu_id"]: self.remover_item(item_id),  # Função de remoção
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    height=30,
                ),
                bgcolor="#1B2C70",
            )
            rows.append(row)

        return ft.Column(
            controls=[*rows],
            spacing=5,  # Espaçamento entre as linhas
            width=800,  # Largura total do cardápio
        )
