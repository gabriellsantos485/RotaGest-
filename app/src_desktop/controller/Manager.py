class Manager:
    """Manager
    Responsável por administrar as chamadas de api do sistema e funções do backend.
    Se comunica com o banco de dados
    Atributos:
    
    Métodos: 
    
    """
    def __init__(self):
        pass
    
    def _payment(self, valueFisinh, url)-> bool:
        """
        Payment
        Método responsável por realizar o pagamento em uma chamada de api do sistema 
        
        Parâmetros: 
        valueFisinh (float): Valor final do pagamento.
        url (str): URL da chamada de api.
        """
        pass
    
    def __verification_of_value(self, valueFisinh)->bool:
        if self.valueFisinh > 0: return True 
        return False

    def _list_items_of_orders(self, id) -> list:
        """
        List items of orders
        Método responsável por retornar a lista de itens dos pedidos.
        """
        pass
    
    def _list_clients(self) -> list:
        """
        List clients
        Método responsável por retornar a lista de clientes.
        """
        pass
    
    def _order_unic(self, id) -> list:
        """
        Orders unic
        Método responsável por retornar a lista de números dos pedidos.
        """
        pass
    
    def _items(self, id) -> dict:
        """
        Items 
        Método responsável por retornar um dicionário com os dados dos itens.
        """
        pass
    
    
    
    