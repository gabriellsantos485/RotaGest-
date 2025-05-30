from restaurante.services.usuario import UsuarioService


class Admin():
    
    list_novo_usuario = []
    
    def __init__(
                self,
                nome: str, 
                sobrenome: str,
                horario_trabalho: str,
                rua:str,
                bairro: str,
                cidade: str,
                estado: str,
                salario: float,
                data_nascimento: str,
                ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horario_trabalho = horario_trabalho
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.salario = salario
        self.data_nascimento = data_nascimento
    
    def cadastrar_usuario(self, usuario):
        self.list_novo_usuario.append(usuario)
        print("Usuario cadastrado com sucesso!!!")
        
    def listar_usuarios(self):
        for usuario in self.list_novo_usuario:
            print(f"Nome do usuario {usuario.username}\nEmail do usuario: {usuario.email}\n Telefone: {usuario.telefone}\n Enredeço de memória: {usuario}")
        
    
    
    