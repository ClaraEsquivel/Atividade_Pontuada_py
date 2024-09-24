from atividade_pontuada.models.endereço import Endereço

class Pessoa(): 
    def __init__(self, id:int, nome:str, telefone:str, email:str, endereço:Endereço) -> None:
        self.id = self.__verificar_id_pessoa(id)
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
       
    def __verificar_id_pessoa(self, id):
        if id < 0:
            raise ValueError("Valor inválido, o ID não pode ser negativo")
        if not isinstance(id, int):
           raise TypeError("Valor inválido")
        return id

    