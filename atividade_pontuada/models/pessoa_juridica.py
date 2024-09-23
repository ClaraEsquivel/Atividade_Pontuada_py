from abc import ABC, abstractmethod
from atividade_pontuada.models.pessoa import Pessoa

class Pessoa_Juridica(ABC):
    def __init__(self, cnpj:str, inscricaoEstadual:str) -> None:
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual

    def __str__(self) -> str:
        return (
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição Estadual: {self.inscricaoEstadual}"
        )