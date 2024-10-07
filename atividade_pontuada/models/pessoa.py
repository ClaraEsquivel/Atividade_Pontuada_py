from atividade_pontuada.models.endereço import Endereço

class Pessoa(): 
    def __init__(self, id:int, nome:str, telefone:str, email:str, endereço:Endereço) -> None:
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereço = endereço
       
       
    def __str__(self) -> str:
        return (
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereço {self.endereço}"
        ) 