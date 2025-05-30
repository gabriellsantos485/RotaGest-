from .empregado import Empregado

class Admin(Empregado):
    
    class Meta:
        managed = False
        
    def cancelar_pedido(self):
        pass
    
    def consultar_vendas(self):
        pass
    
    def consultar_garcoms(self):
        pass
    
    def cadastrar_garcom(self):
        pass
    
    def deletar_garcom(self):
        pass
    