from components.com_appContainer import AppContainer
import flet as ft
from components.textFields import ComandName, ComandNumber
from components.botao import ButtonCategory
from utils.validators import checkout_data_of_fieldName_andFieldCommand
from context.errorsMenssages import ErrorMessages
from context.contextglobals import VarGlobals

fieldName=ComandName()
comandNumber=ComandNumber()

       
class HomeScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        self.base = AppContainer(page) 
        self.buttonCategory=ButtonCategory()
        self.buttonCategory.set_color("#0636AD")
        

    def get_widget(self):
        # Define the dynamic content for the Home screen
        content = ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[fieldName.render()]
                            ),
                            ft.Row(
                                controls=[comandNumber.render()]
                                ),
                            ft.Row(
                                controls=[
                                    self.buttonCategory.renderButtonElevate(new_onclick=self.btn_checkout)
                                    ], alignment=ft.MainAxisAlignment.CENTER),  
                        ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=1
                    ),
             )

        # Return the base container with the dynamic content
        return self.base.build(content)
    
    
    def btn_checkout(self, e):
        if checkout_data_of_fieldName_andFieldCommand(fieldName, comandNumber) == 1:
            VarGlobals.set_name(fieldName.get_value())
            VarGlobals.set_command(comandNumber.get_value())
            return self.page.go("/category")
            
        else:
            #self.page.dialog = ft.AlertDialog(title=ft.Text(ErrorMessages.invalid_input()))
            #self.page.dialog.open = True
            #self.page.update()
            self.base.mensagens_dialog("A comanda deve ser PREENCHIDA para pode seguir!!!")