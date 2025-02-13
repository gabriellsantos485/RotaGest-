import flet as ft
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT
from services.MercadoPago import pay_buy

class OrderPaymentDialog:
    def __init__(self, page: ft.Page, order_id: int, items: list, total_price: float):
        self.page = page
        self.order_id = order_id
        self.items = items
        self.total_price = total_price
        self.dialog = None
        self.total_price = total_price

        # Criar o texto do botão para poder alterá-lo depois
        self.btn_pay_text = ft.Text("Selecionar método de pagamento", color=ft.colors.WHITE, size=18)

    def buildPay(self):
        """
        Builds the AlertDialog for displaying order details and payment options.
        """
        # Responsable for screen of payment 
        screen_paybuy = [
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Card(
                            color="#4D64DB",
                            width=520,
                            height=450,
                            content=ft.Column(
                                controls=[
                                    ft.Row([
                                        ft.Container(
                                            border_radius=10,
                                            margin=10,
                                            padding=10,
                                            bgcolor="#081450",
                                            width=490,
                                            height=70,
                                            content=ft.Column([
                                                ft.Container(
                                                    content=ft.Text(
                                                        "CLIENTE",
                                                        size=10,
                                                        color=ft.colors.WHITE,
                                                        weight=ft.FontWeight.BOLD,
                                                    ),
                                                    width=490,
                                                    height=12
                                                ),
                                                ft.Row([
                                                    ft.Container(
                                                        bgcolor=ft.colors.WHITE,
                                                        width=100,
                                                        height=30,
                                                        content=ft.Text("1", size=24)
                                                    ),
                                                    ft.Container(
                                                        bgcolor=ft.colors.WHITE,
                                                        width=300,
                                                        height=30,
                                                        content=ft.Text("CLIENTE 1", size=24),
                                                    ),
                                                ])
                                            ])
                                        )
                                    ]),
                                    
                                    # Botão de pagamento 
                                    ft.Row([
                                        ft.Container(
                                            border_radius=10,
                                            margin=10,
                                            padding=10,
                                            bgcolor="#081450",
                                            width=490,
                                            height=70,
                                            content=ft.Column([
                                                ft.Container(
                                                    content=ft.Text("FORMA DE PAGAMENTO", color=ft.colors.WHITE, size=12, weight=ft.FontWeight.BOLD),
                                                    width=490,
                                                    height=18        
                                                ),
                                                ft.Container(
                                                    content=ft.PopupMenuButton(
                                                        content=self.btn_pay_text,  # Usa a variável de classe
                                                        items=[
                                                            ft.PopupMenuItem(text="Cartão de Crédito", on_click=self.__selecionar_pagamento),
                                                            ft.PopupMenuItem(text="Pix", on_click=self.__selecionar_pagamento),
                                                            ft.PopupMenuItem(text="Boleto", on_click=self.__selecionar_pagamento),
                                                        ],
                                                        bgcolor=ft.colors.AMBER_100,                                                                                                                    
                                                    ),
                                                    bgcolor="#967FF0",
                                                    width=490,
                                                    height=25,
                                                    border_radius=10
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.START)
                                        )
                                    ]),
                                    
                                    # Total of Order
                                    ft.Row(
                                        [
                                            ft.Container(
                                                width=490,
                                                height=70,
                                                border_radius=10,
                                                bgcolor="#081450",
                                                padding=10,
                                                margin=10,
                                                content=ft.Column(
                                                    [
                                                        ft.Row(
                                                            [
                                                                ft.Text(
                                                                    "TOTAL",
                                                                    size=12,
                                                                    color=ft.colors.WHITE,
                                                                    weight=ft.FontWeight.BOLD
                                                                )
                                                            ]
                                                        ),
                                                        ft.Row(
                                                            [
                                                                ft.Text("R$ 100,00",
                                                                        size=20,
                                                                        color=ft.colors.WHITE,
                                                                        weight=ft.FontWeight.BOLD
                                                                        )
                                                            ],
                                                        alignment=ft.MainAxisAlignment.END
                                                        )
                                                    ]
                                                )
                                            )
                                        ]
                                    ),
                                    
                                    #Button Finish
                                    ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.ElevatedButton(
                                                    content=ft.Text("Finalizar", color=ft.colors.WHITE, size=28),
                                                    bgcolor="#F09013",
                                                    on_click=self._payment,
                                                    width=490,
                                                    height=40,
                                                ),
                                                padding=5,
                                                margin=10
                                            )
                                        ]
                                    )                               ]
                            )
                        ),
                        ft.Card(
                            color=ft.colors.WHITE,
                            width=650,
                            height=450,
                            content=ft.Column(
                                [
                                    ft.Container(
                                        width=650,
                                        height=40,
                                        bgcolor=ft.colors.BLUE_900,
                                        content=ft.Text("Lista de Itens", color=ft.colors.WHITE, size=28, weight=ft.FontWeight.BOLD, text_align="center"), 
                                    ),
                                ]
                            )
                            
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )      
            )
        ] 

        # Criando a caixa de diálogo
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Finalizar Pedido", weight=ft.FontWeight.BOLD),
            content=ft.Container(
                content=ft.Column(screen_paybuy, spacing=10, width=SCREEN_WIDTH * 0.94, height=SCREEN_HEIGHT * 0.94),
                padding=20,
            ),
            actions=[
                ft.TextButton("Fechar", on_click=lambda e: self.close_dialog())
            ],
            bgcolor="#9F9DEF",
        )

        return self.dialog

    def open_dialog(self):
        """Abre o diálogo de pagamento."""
        self.page.dialog = self.buildPay()
        self.page.dialog.open = True
        self.page.update()
    
    def close_dialog(self):
        """Fecha o diálogo de pagamento."""
        if self.dialog:
            self.dialog.open = False
            self.page.update()
    
    def __selecionar_pagamento(self, e):
        """Atualiza o texto do botão para a opção selecionada."""
        self.btn_pay_text.value = e.control.text  # Atualiza o texto do botão
        self.page.update()  # Atualiza a interface
        
    def _payment(self, e):
        """Realiza o pagamento."""
        # Implementar a lógica de pagamento aqui
        resultado = pay_buy(self.total_price)
        print(resultado)
        print("Pagamento realizado com sucesso!")