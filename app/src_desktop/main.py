import flet as ft
from routes.routes import route_manager
from screens.ScreenHome import ScreenHome
from screens.app import AppConfigurator


def main(page: ft.Page):

    AppConfigurator.configure_page(page)
    def on_route_change(e):
        route_manager(page, e.route)  # Passa a rota para o gerenciador

    page.on_route_change = on_route_change

    # Adiciona a tela inicial
    page.views.append(
        ft.SafeArea(
            ft.View(
            route="/",
            controls=[ScreenHome(page).buildHome()
                      ],
        )
        )
    )
    page.go("/")  # Define a rota inicial


if __name__ == "__main__":
    ft.app(target=main)
            
