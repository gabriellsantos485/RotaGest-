"""
Criaçao da classe Produto 

Essa classe sintetiza o que seria produto na  vida real abstraindo dados 
Autor: Gabriel Rodrigues dos Santos
Data: 26/03/2025
"""

class ProdutoService:
    
    def __init__(self,nome):
        self.nome = nome
        self.gramagem = 0.0
        self.litragem = 0.0
        
    @property
    def nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self._nome=novo_nome
        
        
    