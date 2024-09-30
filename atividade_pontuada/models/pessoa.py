from atividade_pontuada.models.endereço import Endereço

class Pessoa(): 
    def __init__(self, id:int, nome:str, telefone:str, email:str, endereço:Endereço) -> None:
        self.id = self.__verificar_id_pessoa(id)
        self.nome = self.__verificar_nome_pessoa(nome)
        self.telefone = self.__verificar_telefone_pessoa(telefone)
        self.email = self.__verificar_email_pessoa(email)
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

            
    def __verificar_nome_pessoa(self, nome):
        if nome == "":
            raise ValueError("O nome não pode ser vazio, você precisa informar o nome!")
        if not isinstance(nome, str):
            raise TypeError("Valor inválido")
        return nome 

    def __verificar_telefone_pessoa(self, telefone):
        if telefone == "":
            raise ValueError("O telefone não pode ser vazio, você precisa informar o telefone!")
        if not isinstance(telefone, str):
            raise TypeError("Valor inválido")
        return telefone

    def __verificar_email_pessoa(self, email):
        if email == "":
            raise ValueError("O email não pode ser vazio, você precisa informar o email!")
        if not isinstance(email, str):
            raise TypeError("Valor inválido")
        return email