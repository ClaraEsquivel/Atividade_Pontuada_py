from atividade_pontuada.models.pessoa import Pessoa
from atividade_pontuada.models.enums.Sexo import Sexo
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.endereço import Endereço

class Pessoa_Fisica(Pessoa):
    def __init__(self, id:int, nome:str, telefone:str, email:str, endereço:Endereço, 
                dataNascimento:str, sexo:Sexo, estadoCivil: EstadoCivil) -> None:
        super().__init__(id=id, nome=nome, telefone=telefone, email=email, endereço=endereço)
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.estadocivil = estadoCivil


    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nData de Nascimento: {self.dataNascimento}"
            f"\nEstado Civil: {self.estadocivil}"
            f"\nSexo: {self.sexo.texto}"
        )   