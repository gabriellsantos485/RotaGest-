import flet as ft
from screens.scr_home import HomeScreen
from screens.scr_category import CategoryScreen
from screens.scr_clients import ClientsScreen
from screens.scr_bag import BagScreen

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
    elif route == "/category":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/category",
                controls=[CategoryScreen(page).get_widget()],
            )
        )
    
    elif route == "/clients":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/category",
                controls=[ClientsScreen(page).get_widget()],
            )
        )
    
    elif route == "/bag":
        page.views.clear()
        page.views.append(
            ft.View(
                route="/category",
                controls=[BagScreen(page).get_widget()],
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