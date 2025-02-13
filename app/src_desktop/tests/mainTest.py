import flet as ft
from components.BasePage import BasePage 


def main(page: ft.Page):
    bp = BasePage(page)

    # Adiciona a tela inicial
    page.views.append(
        ft.SafeArea(
            ft.View(
            route="/",
            controls=[
                    bp.build()
                      ],
        )
        )
    )
    page.go("/")  # Define a rota inicial


if __name__ == "__main__":
    ft.app(target=main)
            
