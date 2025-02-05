from screens.scr_home import HomeScreen
import flet as ft
from screens.scr_menu import Menu
from screens.scr_pedido import Pedido

def route_manager(page: ft.Page, route: str):
    """
    Gerencia as rotas da aplicação.
    Args:
        page (ft.Page): A página principal.
        route (str): A rota atual.
    """
    if route == "/":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[HomeScreen(page).get_widget()],
            )
        )
        
    elif route == "/menu":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/menu",
                controls=[Menu(page).build()],
            )
        )
        
    elif route == "/pedidos":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/pedido",
                controls=[Pedido(page).build()],
            )
        )
        
    elif route == "/pagamento":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/pagamento",
                controls=[ft.Text("Pagamento realizado com sucesso!")],
            )
        )
        
    elif route == "/cancelamento":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/cancelamento",
                controls=[ft.Text("Pedido cancelado com sucesso!")],
            )
        )
    else:
        page.views.clear()
        page.views.append(
            ft.View(
                route="/404",
                controls=[ft.Text("Página não encontrada!")],
            )
        )
    page.update()