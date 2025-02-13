from screens.ScreenHome import ScreenHome
import flet as ft
from screens.ScreenMenu import ScreenMenu
from screens.ScreenOrder import ScreenOrder

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
                controls=[ScreenHome(page).buildHome()],
            )
        )
        
    elif route == "/menu":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/menu",
                controls=[ScreenMenu(page).buildMenu()],
            )
        )
        
    elif route == "/pedidos":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/pedido",
                controls=[ScreenOrder(page).build()],
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