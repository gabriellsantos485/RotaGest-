import flet as ft

class OrderPaymentDialog:
    def __init__(self, page: ft.Page, order_id: int, items: list, total_price: float):
        """
        Creates a payment dialog for an order.
        
        Args:
            page (ft.Page): The main page instance.
            order_id (int): The ID of the order.
            items (list): A list of dictionaries containing item names and quantities.
            total_price (float): The total amount to be paid.
        """
        self.page = page
        self.order_id = order_id
        self.items = items
        self.total_price = total_price
        self.dialog = None

    def build_dialog(self):
        """
        Builds the AlertDialog for displaying order details and payment options.
        """
        
        # Create order details text
        order_details = [ft.Text(f"Pedido #{self.order_id}", weight=ft.FontWeight.BOLD, size=18)]
        
        for item in self.items:
            order_details.append(
                ft.Text(f"{item['name']} x{item['quantity']}", size=18, font_family="Lato")
            )
        
        order_details.append(
            ft.Container(
                content=ft.Text(
                    f"Total: R$ {self.total_price:.2f}", 
                    size=18, 
                    color=ft.colors.BLUE,
                    text_align="center"
                ),
            )
        )
        
        # Payment button
        payment_button = ft.TextButton(
            "Escolher Forma de Pagamento",
            on_click=self.handle_payment_selection,
            width=250,
            height=40,
        )
        
        # Create the dialog
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Pagamento do Pedido", weight=ft.FontWeight.BOLD),
            content=ft.Container(
                content=ft.Column(order_details + [payment_button], spacing=10, width=700),
                padding=20,
                bgcolor=ft.colors.AMBER_50,
                
            ),
            actions=[
                ft.TextButton("Fechar", on_click=lambda e: self.close_dialog())
            ],
            bgcolor=ft.colors.WHITE70,
        )
        
        return self.dialog

    def open_dialog(self):
        """
        Opens the payment dialog.
        """
        self.page.dialog = self.build_dialog()
        self.page.dialog.open = True
        self.page.update()
    
    def close_dialog(self):
        """
        Closes the payment dialog.
        """
        if self.dialog:
            self.dialog.open = False
            self.page.update()
    
    def handle_payment_selection(self, e):
        """
        Handles the selection of the payment method.
        """
        print("Redirecting to payment selection...")
        # Here, you can navigate to another screen or open another dialog.
        self.close_dialog()

# ============================= GUIDE =============================
# How to use OrderPaymentDialog:
#
# 1. Initialize the dialog with order details:
#    payment_dialog = OrderPaymentDialog(page, order_id=123, items=[
#        {'name': 'Burger', 'quantity': 2},
#        {'name': 'Soda', 'quantity': 1}
#    ], total_price=25.50)
#
# 2. Open the dialog when needed:
#    payment_dialog.open_dialog()
#
# 3. The user will see the order details and a button to select payment.
# 4. Clicking the button will trigger `handle_payment_selection()`, which can be customized.
# 5. The user can close the dialog at any time using the "Fechar" button.
# =================================================================
