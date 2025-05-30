import flet as ft
from config.constant import SCREEN_WIDTH, SCREEN_HEIGHT
from services.MercadoPago import pay_buy
from services.APIClient import APIClient

class OrderPaymentDialog:
    def __init__(self, page: ft.Page, order_id: int, items: list, total_price: float) -> None:
        self.page = page
        self.order_id = order_id
        self.items = items
        self.total_price = total_price
        self.dialog = None
        self.api = APIClient()

        # Inicializa o método de pagamento
        self.payment_method = None

        # Criar o texto do botão para poder alterá-lo depois
        self.btn_pay_text = ft.Text("Selecionar método de pagamento", color=ft.colors.WHITE, size=18)

        # Campo para entrada de valor pago (inicialmente invisível)
        self.cash_input = ft.TextField(
            label=ft.Text(value="Valor", color=ft.colors.BLACK, size=18), 
            visible=False, 
            keyboard_type=ft.KeyboardType.NUMBER,
            on_change=self._calculate_change,
            bgcolor=ft.colors.WHITE
        )

        # Exibir o troco (inicialmente invisível)
        self.change_text = ft.Text("", color=ft.colors.WHITE, size=24, visible=False, weight=ft.FontWeight.BOLD)

    def buildPay(self) -> ft.AlertDialog:
        """
        Builds the AlertDialog for displaying order details and payment options.
        """
        screen_paybuy = [
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Card(
                            color="#1E3A8A",
                            width=520,
                            height=500,  # Aumentei a altura para caber o novo campo
                            content=ft.Column(
                                controls=[
                                    # Seção do Cliente
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
                                    
                                    # Método de Pagamento
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
                                                        content=self.btn_pay_text,  
                                                        items=[
                                                            ft.PopupMenuItem(text="Cartão de Crédito", on_click=self.__selecionar_pagamento),
                                                            ft.PopupMenuItem(text="Pix", on_click=self.__selecionar_pagamento),
                                                            ft.PopupMenuItem(text="Boleto", on_click=self.__selecionar_pagamento),
                                                            ft.PopupMenuItem(text="Dinheiro", on_click=self.__selecionar_pagamento),  # Adicionando Dinheiro
                                                        ],
                                                        bgcolor=ft.colors.AMBER_100,                                                                                                                    
                                                    ),
                                                    bgcolor="#967FF0",
                                                    width=490,
                                                    height=25,
                                                    border_radius=10
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.START)
                                        )
                                    ]),

                                    # Total do Pedido
                                    ft.Row([
                                        ft.Container(
                                            width=490,
                                            height=70,
                                            border_radius=10,
                                            bgcolor="#081450",
                                            padding=10,
                                            margin=10,
                                            content=ft.Column([
                                                ft.Row([
                                                    ft.Text("TOTAL", size=12, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)
                                                ]),
                                                
                                                ft.Row([
                                                    ft.Text(
                                                            f"R$ {float(self.total_price):.2f}" if self.total_price is not None else f"R$ {(self.total_price)}",
                                                            size=20,
                                                            color=ft.colors.WHITE,
                                                            weight=ft.FontWeight.BOLD
                                                    )
                                                ], alignment=ft.MainAxisAlignment.END)
                                            ])
                                        )
                                    ]),

                                    # Campo de Entrada para Dinheiro (inicialmente invisível)
                                    self.cash_input,

                                    # Texto do troco (inicialmente invisível)
                                    self.change_text,

                                    # Botão Finalizar
                                    ft.Row([
                                        ft.Container(
                                            content=ft.ElevatedButton(
                                                content=ft.Text("Finalizar", color=ft.colors.WHITE, size=28),
                                                bgcolor="#10B981",
                                                on_click=self._payment,
                                                width=490,
                                                height=40,
                                            ),
                                            padding=5,
                                            margin=10
                                        )
                                    ]),  
                                ]    
                            )
                        )
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
            bgcolor="#F3F4F6",
        )

        return self.dialog

    def open_dialog(self) -> None:
        """Abre o diálogo de pagamento."""
        self.page.dialog = self.buildPay()
        self.page.dialog.open = True
        self.page.update()
    
    def close_dialog(self)->None:
        """Fecha o diálogo de pagamento."""
        if self.dialog:
            self.dialog.open = False
            self.page.update()
    
    def __selecionar_pagamento(self, e) -> None:
        """Atualiza o texto do botão e armazena a opção escolhida."""
        self.payment_method = e.control.text  # Armazena a opção escolhida
        self.btn_pay_text.value = self.payment_method  
        self.page.update()
        
    def _payment(self, e)-> None:
        
        """Realiza o pagamento."""
        if self.payment_method == "Dinheiro":
            self.cash_input.visible = True  # Exibe o campo de entrada
            self.change_text.visible = True  # Exibe o texto do troco
            self.page.update()
            value=self.cash_input.value
            
            if value != "":
                alert = ft.AlertDialog(
                    title=ft.Text("Atenção", weight=ft.FontWeight.BOLD, size=24),
                    content=ft.Text("Pagamento Realizado com Sucesso!!!", size=18),
                    actions=[ft.TextButton("OK", on_click=self.close_dialog())]
                    
                )
                self.page.dialog = alert
                self.page.dialog.open = True
                self.page.update()
                self.api.update_pedido_status(self.order_id, "F")
        
        elif self.payment_method == "Pix":
            pass
        
        else:
            resultado = pay_buy(self.total_price)
            # print(resultado)
            # print("Pagamento realizado com sucesso!")
        
    def _calculate_change(self, e)-> None:
        """Calcula o troco e exibe."""
        try:
            paid_amount = float(self.cash_input.value)
            change = paid_amount - self.total_price
            self.change_text.value = f"Troco: R$ {change:.2f}" if change >= 0 else "Valor insuficiente!"
        except ValueError:
            self.change_text.value = "Digite um valor válido."
        
        self.page.update()
