from abc import ABC, abstractmethod
from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.enums.Sexo import Sexo
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil

class Pessoa_Fisica(ABC):
    def __init__(self, dataNascimento:str, sexo:Sexo, estadocivil: EstadoCivil) -> None:
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.estadocivil = estadocivil


    def __str__(self) -> str:
        return (
            f"\nData de Nascimento: {self.dataNascimento}"
            f"\nEstado Civil: {self.estadocivil}"
            f"\nSexo: {self.sexo.texto}"
        )   