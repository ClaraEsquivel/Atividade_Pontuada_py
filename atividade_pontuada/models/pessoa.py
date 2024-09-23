from abc import ABC, abstractmethod
from atividade_pontuada.models.endereço import Endereço

class Pessoa(ABC): 
    def __init__(self, nome:str, telefone:str, email:str, endereço:Endereço) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereço = endereço

    def __str__(self) -> str:
        return (
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereço {self.endereço}"
        )    