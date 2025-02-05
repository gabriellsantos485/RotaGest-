import flet as ft
from components.com_appContainer import AppContainer
from components.botoes import Button
from services.api import Api

class CriarMenu:
    def __init__(self, page):
        self.page = page
        self.base = AppContainer(page)
        self.btn_salvar = Button(page=page, color="#19721C")
        self.btn_salvar.set_onclick(self.salvar_dados)
        self.bgcolor = "white"
        self.__value_valor=None
        self.__value_nome=None
        self.__value_categoria=None
        self.api = Api(page)
        
        # Criar referências para os campos
        self.nome_ref = ft.Ref[ft.TextField]()
        self.valor_ref = ft.Ref[ft.TextField]()
        self.categoria_ref = ft.Ref[ft.Dropdown]()
        
        
    def __data(self, nome, valor, cat):
        data = {
            'menu_nome': nome,
            'menu_valor': valor,
            'cat_id': self.api._get_id_categoria(cat),
            'menu_imagem': None
        }
        return data
            
    def salvar_dados(self, e):
        """
        Função chamada ao clicar no botão Salvar.
        Obtém os valores preenchidos nos campos e realiza o processamento.
        """
        nome = self.nome_ref.current.value
        valor = self.valor_ref.current.value
        categoria = self.categoria_ref.current.value
        
        if not nome or not valor or not categoria:
            self.base.show_message("Preencha todos os campos!", "red")
        else:
        # Envio dos dados para a API
            self.api.set_api(self.__data(nome, valor, categoria))
            # Resetar os campos
            self.nome_ref.current.value = ""
            self.valor_ref.current.value = ""
            self.categoria_ref.current.value = None

            # Atualizar a interface para refletir os valores resetados
            self.page.update()

    def build(self):
        content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.TextField(
                                label="Nome",
                                width=650,
                                height=50,
                                bgcolor=self.bgcolor,
                                border_radius=20,
                                ref=self.nome_ref,  # Referência ao campo Nome,
                                value=self.__value_nome
                            ),  
                        ],
                        alignment="center"
                    ),
                    ft.Row(
                        controls=[
                            ft.TextField(
                                label="Valor",
                                width=650,
                                height=50,
                                bgcolor=self.bgcolor,
                                keyboard_type=ft.KeyboardType.NUMBER,
                                border_radius=20,
                                ref=self.valor_ref,  # Referência ao campo Valor
                                value=self.__value_valor
                            )
                        ],
                        alignment="center"
                    ),
                    ft.Row(
                        controls=[
                            ft.Dropdown(
                                width=300,
                                options=[
                                    ft.dropdown.Option(i["cat_nome"]) for i in self.api.get_api("http://127.0.0.1:8000/api/categorias/")
                                ],
                                bgcolor="#AB40A9",
                                border_radius=20,
                                label=ft.Text(value="Categoria", weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.CENTER),
                                color="black",
                                ref=self.categoria_ref,  # Referência ao campo Categoria
                                value=self.__value_categoria
                            )
                        ],
                        alignment="center"
                    ),
                    ft.Row(
                        controls=[
                            self.btn_salvar.build("Salvar")  # Associar o evento de clique
                        ],
                        alignment="center"
                    )
                ],
                alignment="center",
                spacing=40
            ),
            bgcolor="#22094D"
        )
        
        return self.base.build(content=content)


    def set_value_categoria(self, new_cat):
        self.__value_categoria = new_cat
        
    def set_value_nome(self, new_nam):
        self.__value_nome=new_nam
        
    def set_value_valor(self, new_val):
        self.__value_valor = new_val