"""
Classe Usuario, abstrai o usuario do mundo real para um objeto
com metodos e comportamentos

Autor: Gabriel Rodrigues dos Santos
Data: 26/03/2025
"""


from restaurante.models.usuario import Usuario


class UsuarioService:
    def __init__(self, 
                 telefone: str,
                 email: str,
                 password: str,
                 username: str,
                 ):
        self.telefone = telefone
        self.email = email
        self.password = password
        self.username = username
        
    def efetuar_pedido(self, pedido):
        """Methodo criado para efetuar um pedido
        
        Recebe um pedido como parametro que salva no banco de dados """
        pass
    
    def vizualizar_cardapio(self):
        """
        Methodo criado para vizualizar o cardapio do sistema 
        
        Não recebe parametro e retorna todo o cardapio 
        """
        pass
    
    def vizualizar_estoque(self):
        """
        Retorna todo o estoque para o garçon
        """
        
    def vizualizar_pedidos(self):
        """Methodo para vizualizar os pedidos dentro do sistema"""
        
    def vizualizar_pedido(self, id_pedido):
        """Vizualizar um unico pedido especifico"""
        
    def verificar_comanda(self, id_comanda):
        """Verifica o status da comanda e retorna o cliente alocado nela"""
        
    def cadastrar_novo_cliente(self):
        """Cadastra um novo cliente dentro do sistema"""
        
    def verificar_status_do_pedido(self):
        """Verifica quando um pedido está pronto, em preparo ou cancelado"""
    
    def __tirar_do_estoque(self):
        """Methodo para cozinha"""
        
            
    
        
    
   
    
    