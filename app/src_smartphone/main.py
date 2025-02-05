import flet as ft
from screens.app import AppConfigurator
from components.com_appContainer import AppContainer
from routes.routes import route_manager
from screens.scr_home import HomeScreen
    
def main(page: ft.Page):
    """
    Função principal que inicializa a aplicação Flet.
    """
    # Configura a página
    AppConfigurator.configure_page(page)
    page.title = ""
    app_container = AppContainer(page)
    page.theme_mode=ft.ThemeMode.DARK
    page.fonts = {
        "Open Sans": "/font3s/OpenSans-Regular.ttf"
    }

    # Gerenciamento de rotas
    def on_route_change(e):
        route_manager(page, e.route)  # Passa a rota para o gerenciador

    page.on_route_change = on_route_change

    # Adiciona a tela inicial
    page.views.append(
        ft.SafeArea(
            ft.View(
            route="/",
            controls=[HomeScreen(page).get_widget()],
        )
        )
    )
    page.go("/")  # Define a rota inicial


if __name__ == "__main__":
    ft.app(main)
            
