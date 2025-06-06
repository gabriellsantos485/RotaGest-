import flet as ft
from components.BasePage import BasePage
from components.botoes import Button
from utils.cadastro import cadastrar_categoria


class LayoutCategory(BasePage):
    
    def __init__(self,  page: ft.Page):
        """
        Inicializa a classe ListarMenu com a página principal.

        Args:
            page (ft.Page): Página principal da aplicação.
        """
        super().__init__(page)
        self.page = page
        self.btn=Button(page=page, color="#1019C2")
        self.btn.set_onclick(onclick=self.salvar_categoria)
        self.categoria_ref = ft.Ref[ft.TextField]()  # Criando a referência para o TextField
        

    def salvar_categoria(self, e):
        # Acessa o valor do TextField
        categoria = self.categoria_ref.current.value
        return cadastrar_categoria(categoria, self.page)
    
    def content(self):
        return ft.Container(
            content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.TextField(label="Nome da Categoria", width=450, height=40, bgcolor="white", color="black", ref=self.categoria_ref),
                            ],
                            alignment="center"
                        ), 
                        ft.Row(
                            controls=[self.btn.build("Salvar")],
                            alignment="center"
                        )
                    ],
                    alignment="center",
                    spacing=100
                ),
            bgcolor="#22094D",
            
        )