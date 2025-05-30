from django.test import TestCase

from restaurante.services.admin import Admin
from restaurante.services.usuario import UsuarioService



class TestAdmin(TestCase):
    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        self.gabriel = Admin( 
                             "Gabriel",
                             "Rodrigues",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",
                             "",     
                             )
        
        self.usu_maria = UsuarioService("11 987574511","maria@gmail", "12334", "maria")
        self.usu_joao = UsuarioService("11 987574511","joao@gmail", "12334", "joao")
        
    #def test_cadastrar_usuario(self):
        
        #self.gabriel.cadastrar_usuario()
        
        #self.assertEqual(gabriel.email, "gabriel.santos@gmail.com")
    
    def test_cadastrar_usuario(self):
        self.gabriel.cadastrar_usuario(usuario=self.usu_maria)
        self.gabriel.cadastrar_usuario(self.usu_joao)
        
    def test_listar_usuario(self):
        self.gabriel.listar_usuarios()