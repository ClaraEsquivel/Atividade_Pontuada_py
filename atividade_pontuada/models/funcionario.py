from atividade_pontuada.models.enums.Setor import Setor
from atividade_pontuada.models.enums.EstadoCivil import EstadoCivil
from atividade_pontuada.models.enums.Sexo import Sexo
from atividade_pontuada.models.pessoa_fisica import Pessoa_Fisica
from atividade_pontuada.models.endereço import Endereço


class Funcionario(Pessoa_Fisica):
    def __init__(self, id:int, nome:str, telefone:str, email:str, endereco:Endereço,
                 sexo:Sexo, estadoCivil:EstadoCivil, dataNascimento:str, cpf:str, rg:str, 
                 matricula:str, setor:Setor, salario:float) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor.texto}"
            f"\nSalário: {self.salario}"

        )
    