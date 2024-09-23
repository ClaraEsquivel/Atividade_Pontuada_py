from abc import ABC, abstractmethod
from atividade_pontuada.models.enums.Setor import Setor

class Funcionario(ABC):
    def __init__(self, cpf:str, rg:str, matricula:str, setor:Setor, salario:float) -> None:
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        return (
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor.texto}"
            f"\nSalário: {self.salario}"

        )