import flet as ft
from config.constant import FONT, SCREEN_HEIGHT, SCREEN_WIDTH
from components.com_appContainer import AppContainer

class BagData:
    def __init__(self, page: str, items: list[dict]):
        """
        Classe para renderizar e gerenciar dados de uma sacola.

        Args:
            page (str): Página de origem.
            items (list[dict]): Lista de dicionários com os dados dos itens.
                Cada dicionário deve ter as chaves:
                - "name" (str): Nome do item.
                - "quantity" (int): Quantidade do item.
        """
        self.page = page
        self.items = items
        self.base = AppContainer(page)

    def render(self) -> ft.Container:
        """
        Renderiza a sacola como uma lista de linhas com informações dos itens.

        Returns:
            ft.Container: Contêiner com os dados renderizados.
        """
        rows = []
        for idx, item in enumerate(self.items):
            rows.append(
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                value=str(item["count"]),
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.WHITE
                            ),
                            ft.Text(
                                value=item["name"],
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.WHITE,
                                font_family=FONT                           
                            ),
                            ft.Text(
                                value=f"R$ {item['value']:.2f}",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.WHITE
                                ),
                            
                            ft.IconButton(
                                icon=ft.icons.DELETE_FOREVER_ROUNDED,
                                on_click=lambda e, i=idx: self.delete_of_list(i),
                                icon_color=ft.colors.RED
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        
                    ),
                    bgcolor="#3668E4",
                    width=SCREEN_WIDTH * 0.90,
                    padding=10,
                    margin=10,
                    border_radius=10
                    
                )
            )

        # Retorna o Container contendo as linhas geradas
        return ft.Container(
            content=ft.Column(
                controls=rows,
                spacing=10,
                expand=True,
                scroll="auto",
                height=SCREEN_HEIGHT *0.65
            )
        )

    def delete_of_list(self, index: int):
        """
        Remove um item da lista baseado no índice.

        Args:
            index (int): Índice do item a ser removido.
        """
        if 0 <= index < len(self.items):
            # Remover o item da lista compartilhada
            del self.items[index]
            self.page.controls.clear()  # Limpa todos os controles existentes
            self.page.add(self.render())  # Recria a interface com a lista atualizada
            self.page.update()  # Atualiza a página no Flet
